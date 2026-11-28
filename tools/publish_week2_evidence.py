#!/usr/bin/env python3
"""Fail-closed validator and draft GitHub Release uploader for BL4S Week 2."""
import argparse
import base64
import csv
import hashlib
import json
import os
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import PurePosixPath

import requests

REPO = "MahmutVezir/bl4s-2027-electron-scattering"
BRANCH = "submission/week2-boundary-evidence-structure-2026-11-28"
PR = 6
SOURCE_COMMIT = "08abe699f7e49da430acb8830fda2ae1a1f926ae"
SEEDS = {"air": [271828, 314159], "aluminium": [161803, 141421]}
MISSES = {"air": [1191], "aluminium": []}
EVENTS = 2000


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_member(zf, name):
    h = hashlib.sha256()
    with zf.open(name) as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(zf, name):
    value = json.loads(zf.read(name).decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Expected JSON object: " + name)
    return value


def csv_count(zf, name):
    with zf.open(name) as raw:
        rows = csv.reader(line.decode("utf-8-sig") for line in raw)
        header = next(rows, None)
        if not header or len(set(header)) != len(header):
            raise ValueError("Invalid CSV header: " + name)
        return sum(1 for row in rows if row)


def validate(path):
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        raise FileNotFoundError("Archive not found or empty: " + path)
    if os.path.getsize(path) > 2 * 1024**3:
        raise ValueError("Archive exceeds 2 GiB")
    with zipfile.ZipFile(path) as z:
        infos = [i for i in z.infolist() if not i.is_dir()]
        names = [i.filename for i in infos]
        if len(names) != len(set(names)):
            raise ValueError("Duplicate ZIP paths")
        for n in names:
            p = PurePosixPath(n)
            if p.is_absolute() or ".." in p.parts or "\\" in n:
                raise ValueError("Unsafe ZIP path: " + n)
        bad = z.testzip()
        if bad:
            raise ValueError("ZIP CRC failure: " + bad)

        required = ["production_manifest.json", "root_export_manifest.json",
                    "week2_boundary_production.root"]
        for n in required:
            if n not in names:
                raise ValueError("Missing required archive member: " + n)

        prod = read_json(z, "production_manifest.json")
        if prod.get("source_commit") != SOURCE_COMMIT:
            raise ValueError("Production source commit does not match pinned source")
        if prod.get("geant4_version") != "11.4.3":
            raise ValueError("Expected Geant4 11.4.3 in production manifest")
        if prod.get("events_per_condition") != EVENTS:
            raise ValueError("Expected 2,000 events per condition")
        if prod.get("theta_formula") != "acos(clip(u_entry dot u_exit, -1, 1)) * 1000 mrad":
            raise ValueError("Target-angle definition mismatch")
        if prod.get("energy_loss_formula") != "kinetic_energy_entry - kinetic_energy_exit (MeV)":
            raise ValueError("Energy-loss definition mismatch")

        stats_all = prod.get("conditions")
        if not isinstance(stats_all, dict):
            raise ValueError("Missing production conditions object")
        row_counts = {}
        for c in ("air", "aluminium"):
            s = stats_all.get(c)
            if not isinstance(s, dict):
                raise ValueError("Missing condition: " + c)
            if s.get("events_generated") != EVENTS or s.get("seeds") != SEEDS[c]:
                raise ValueError("Event count or seed mismatch for " + c)
            if s.get("missed_event_ids") != MISSES[c]:
                raise ValueError("Missed-event IDs do not match the frozen seed run for " + c)
            crossing = s.get("events_crossing_target")
            misses = s.get("events_not_crossing_target")
            if not isinstance(crossing, int) or not isinstance(misses, int) or crossing + misses != EVENTS:
                raise ValueError("Incomplete crossing/miss accounting for " + c)

            required_csv = {
                "hits.csv": s.get("hits"),
                "tracks.csv": s.get("track_steps"),
                "target_boundaries.csv": s.get("boundary_records"),
                "target_boundary_analysis.csv": crossing,
            }
            for fn, expected in required_csv.items():
                member = c + "/" + fn
                if member not in names:
                    raise ValueError("Missing CSV: " + member)
                actual = csv_count(z, member)
                if actual != expected:
                    raise ValueError(f"{member}: {actual} rows, expected {expected}")
                row_counts[member] = actual

            cm = read_json(z, c + "/condition_manifest.json")
            if cm.get("condition") != c or not isinstance(cm.get("sha256"), dict):
                raise ValueError("Invalid condition manifest: " + c)
            for fn, expected_hash in cm["sha256"].items():
                member = c + "/" + fn
                if member not in names or sha256_member(z, member) != expected_hash:
                    raise ValueError("Condition file SHA-256 mismatch: " + member)

        rm = read_json(z, "root_export_manifest.json")
        root_name = "week2_boundary_production.root"
        root_info = z.getinfo(root_name)
        root_sha = sha256_member(z, root_name)
        if rm.get("root_file") != root_name or rm.get("sha256") != root_sha:
            raise ValueError("ROOT SHA-256 does not match ROOT export manifest")
        if rm.get("size_bytes") != root_info.file_size or rm.get("tree_count") != 8:
            raise ValueError("ROOT size or TTree count mismatch")
        if rm.get("roundtrip") != "all branches matched CSV arrays exactly":
            raise ValueError("CSV/ROOT branch round-trip is not declared successful")
        trees = rm.get("trees")
        if not isinstance(trees, dict) or len(trees) != 8:
            raise ValueError("ROOT manifest must list all eight TTrees")
        for c in ("air", "aluminium"):
            for kind, fn in (("hits", "hits.csv"), ("tracks", "tracks.csv"),
                             ("boundaries", "target_boundaries.csv"),
                             ("analysis", "target_boundary_analysis.csv")):
                key = c + "_" + kind
                if trees.get(key) != row_counts[c + "/" + fn]:
                    raise ValueError("ROOT TTree entry count mismatch: " + key)
        total = sum(trees.values())
        if rm.get("total_tree_entries") != total:
            raise ValueError("Total ROOT entry count mismatch")

        reports = sorted(n for n in names if re.fullmatch(
            r"root_outlier_trace_report(?:_\d{8}T\d{6}Z)?\.json", n))
        if not reports:
            raise ValueError("No timestamped outlier trace report found")

        # Repeated audits are allowed only if all reports and their supporting
        # candidate/trace artifacts are byte-equivalent for the same ROOT file.
        audit_records = []
        for report_name in reports:
            report = read_json(z, report_name)
            if report.get("root_sha256") != root_sha or not report.get("traced_event_ids"):
                raise ValueError("Outlier report does not match ROOT file or has no traces")

            candidate = report.get("candidate_csv")
            trace_dir = str(report.get("trace_directory", "")).rstrip("/")
            trace_prefix = trace_dir + "/"
            if candidate not in names or not trace_dir:
                raise ValueError("Outlier candidate CSV or trace folder is missing")
            if not any(n.startswith(trace_prefix) for n in names):
                raise ValueError("Outlier trace folder is missing: " + trace_dir)

            relative_files = sorted(
                n[len(trace_prefix):] for n in names
                if n.startswith(trace_prefix) and not n.endswith("/")
            )
            if not relative_files:
                raise ValueError("No event trace files found: " + trace_dir)

            event_dirs = sorted({
                rel.split("/", 1)[0] for rel in relative_files if "/" in rel
            })
            if not event_dirs:
                raise ValueError("No event trace folders found: " + trace_dir)

            expected_files = {
                event + "/" + fn
                for event in event_dirs
                for fn in ("boundaries.csv", "hits.csv", "tracks.csv", "analysis.csv")
            }
            if set(relative_files) != expected_files:
                raise ValueError("Incomplete or unexpected event trace files: " + trace_dir)

            traced_ids_from_dirs = sorted(
                int(event.removeprefix("event_")) for event in event_dirs
                if re.fullmatch(r"event_\d+", event)
            )
            if traced_ids_from_dirs != sorted(report["traced_event_ids"]):
                raise ValueError("Trace folder event IDs do not match the report: " + report_name)

            normalized_report = {
                key: value for key, value in report.items()
                if key not in ("candidate_csv", "trace_directory")
            }
            trace_hashes = {
                rel: sha256_member(z, trace_prefix + rel)
                for rel in relative_files
            }
            audit_records.append({
                "report_name": report_name,
                "normalized_report": normalized_report,
                "candidate_sha256": sha256_member(z, candidate),
                "trace_hashes": trace_hashes,
                "event_dirs": event_dirs,
            })

        canonical = audit_records[0]
        for duplicate in audit_records[1:]:
            if duplicate["normalized_report"] != canonical["normalized_report"]:
                raise ValueError("Duplicate outlier reports contain different scientific content")
            if duplicate["candidate_sha256"] != canonical["candidate_sha256"]:
                raise ValueError("Duplicate outlier candidate CSV files differ")
            if duplicate["trace_hashes"] != canonical["trace_hashes"]:
                raise ValueError("Duplicate outlier event trace files differ")
            if duplicate["event_dirs"] != canonical["event_dirs"]:
                raise ValueError("Duplicate outlier event trace folders differ")

        report = read_json(z, canonical["report_name"])
        event_dirs = canonical["event_dirs"]

    return {
        "repository": REPO,
        "branch": BRANCH,
        "pr_number": PR,
        "archive_name": os.path.basename(path),
        "archive_size_bytes": os.path.getsize(path),
        "archive_sha256": sha256_file(path),
        "validation": "PASS",
        "source_commit": SOURCE_COMMIT,
        "geant4_version": prod["geant4_version"],
        "events_per_condition": EVENTS,
        "condition_statistics": stats_all,
        "root_file": root_name,
        "root_size_bytes": root_info.file_size,
        "root_sha256": root_sha,
        "root_tree_count": rm["tree_count"],
        "root_total_tree_entries": total,
        "outlier_trace_report": reports[0],
        "outlier_trace_reports": reports,
        "outlier_trace_report_count": len(reports),
        "duplicate_audit_reports_verified_identical": True,
        "traced_event_folders": event_dirs,
        "notes": [
            "Geant4 Monte Carlo evidence, not CERN beam-time data.",
            "Air and aluminium are independent samples; event IDs are not paired.",
            "Outlier candidates are retained with trace evidence.",
        ],
    }


def gh(method, url, token, **kwargs):
    headers = kwargs.pop("headers", {})
    headers.update({"Authorization": "Bearer " + token,
                    "Accept": "application/vnd.github+json",
                    "X-GitHub-Api-Version": "2022-11-28"})
    r = requests.request(method, url, headers=headers, timeout=120, **kwargs)
    if not r.ok:
        raise RuntimeError(f"GitHub API {method} failed ({r.status_code}): {r.text[:1500]}")
    return r


def publish(path, inv):
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        raise RuntimeError("Set GITHUB_TOKEN through Colab Secrets; never hard-code it")
    base = "https://api.github.com/repos/" + REPO
    pr = gh("GET", base + "/pulls/" + str(PR), token).json()
    if pr.get("state") != "open" or pr.get("merged"):
        raise RuntimeError("PR #6 must remain open and unmerged")
    if pr.get("base", {}).get("ref") != "main" or pr.get("head", {}).get("ref") != BRANCH:
        raise RuntimeError("PR #6 branches do not match expected Week 2 branches")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    tag = "week2-boundary-evidence-" + stamp + "-" + inv["archive_sha256"][:8]
    body = (
        "Validated Week 2 Geant4 target-boundary evidence. DRAFT FOR REVIEW. "
        "Simulation outputs only; not CERN beam-time data. Air/aluminium are independent "
        "samples. Outlier candidates are retained.\\n\\n"
        + "Archive SHA-256: " + inv["archive_sha256"] + "\\n"
        + "ROOT SHA-256: " + inv["root_sha256"] + "\\n"
        + "Source commit: " + SOURCE_COMMIT
    )
    rel = gh("POST", base + "/releases", token, json={
        "tag_name": tag, "target_commitish": BRANCH,
        "name": "Week 2 boundary evidence " + stamp,
        "body": body, "draft": True, "prerelease": True
    }).json()
    sidecar = path + ".sha256"
    inventory_path = path + ".inventory.json"
    with open(sidecar, "w", encoding="utf-8") as f:
        f.write(inv["archive_sha256"] + "  " + os.path.basename(path) + "\\n")
    with open(inventory_path, "w", encoding="utf-8") as f:
        json.dump(inv, f, indent=2, ensure_ascii=False)
        f.write("\\n")
    upload_url = rel["upload_url"].split("{", 1)[0]
    assets = []
    for p, mime in ((path, "application/zip"), (sidecar, "text/plain"),
                    (inventory_path, "application/json")):
        with open(p, "rb") as f:
            a = gh("POST", upload_url, token, params={"name": os.path.basename(p)},
                   data=f, headers={"Content-Type": mime}).json()
        assets.append({"name": a.get("name"), "size": a.get("size"),
                       "url": a.get("browser_download_url")})
    receipt = {
        "release_tag": tag, "release_url": rel.get("html_url"),
        "release_is_draft": rel.get("draft"), "pr_url": pr.get("html_url"),
        "archive_name": os.path.basename(path),
        "archive_size_bytes": inv["archive_size_bytes"],
        "archive_sha256": inv["archive_sha256"],
        "root_sha256": inv["root_sha256"], "source_commit": SOURCE_COMMIT,
        "assets": assets, "created_at_utc": datetime.now(timezone.utc).isoformat()
    }
    receipt_path = "results/week2/releases/" + tag + ".json"
    content = base64.b64encode((json.dumps(receipt, indent=2, ensure_ascii=False) + "\\n").encode()).decode()
    gh("PUT", base + "/contents/" + receipt_path, token, json={
        "message": "Register Week 2 evidence release " + tag,
        "content": content, "branch": BRANCH
    })
    return receipt


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archive", required=True, help="Exact ZIP path printed by notebook Stage 7")
    ap.add_argument("--publish-draft", action="store_true",
                    help="After validation, upload assets to a draft GitHub Release and write a PR-branch receipt")
    args = ap.parse_args()
    inv = validate(args.archive)
    sha_path, inventory_path = args.archive + ".sha256", args.archive + ".inventory.json"
    with open(sha_path, "w", encoding="utf-8") as f:
        f.write(inv["archive_sha256"] + "  " + os.path.basename(args.archive) + "\\n")
    with open(inventory_path, "w", encoding="utf-8") as f:
        json.dump(inv, f, indent=2, ensure_ascii=False)
        f.write("\\n")
    print("WEEK 2 ARCHIVE VALIDATION: PASS")
    print(json.dumps(inv, indent=2, ensure_ascii=False))
    print("SHA sidecar:", sha_path)
    print("Inventory:", inventory_path)
    if args.publish_draft:
        receipt = publish(args.archive, inv)
        print("DRAFT RELEASE CREATED")
        print(json.dumps(receipt, indent=2, ensure_ascii=False))
    else:
        print("Validation only. Review the report, then rerun with --publish-draft.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("ERROR:", type(exc).__name__, str(exc), file=sys.stderr)
        raise SystemExit(2)
