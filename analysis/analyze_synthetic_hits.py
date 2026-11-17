"""NumPy and Matplotlib analysis of the synthetic hit sample.
Run from repository root after installing numpy and matplotlib:
python analysis/analyze_synthetic_hits.py
The sample is pedagogical, not CERN beam data.
"""
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/synthetic/example_hits.csv"
SUMMARY = ROOT / "data/synthetic/summary.csv"
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)
data = np.genfromtxt(INPUT, delimiter=",", names=True, dtype=None, encoding="utf-8")
conditions = ["reference_no_target", "aluminium_foil"]
results = {}

for condition in conditions:
    values = data["x_mm"][data["condition"] == condition].astype(float)
    n = values.size
    mean = np.mean(values)
    sample_std = np.std(values, ddof=1)
    sem = sample_std / np.sqrt(n)
    results[condition] = {"n": n, "mean": mean, "sample_std": sample_std, "sem": sem}
    print(f"{condition}: n={n}, mean={mean:.5f} mm, sample SD={sample_std:.5f} mm, SEM={sem:.5f} mm")

with SUMMARY.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["condition", "n", "mean_x_mm", "sample_std_mm", "standard_error_mm"])
    for condition, result in results.items():
        writer.writerow([condition, result["n"], f'{result["mean"]:.6f}', f'{result["sample_std"]:.6f}', f'{result["sem"]:.6f}'])

fig, ax = plt.subplots(figsize=(9, 5.5))
for condition, label in [("reference_no_target", "No-target reference"), ("aluminium_foil", "Aluminium foil (synthetic)")]:
    values = data["x_mm"][data["condition"] == condition].astype(float)
    ax.hist(values, bins=25, range=(-2.5, 2.5), alpha=0.58, label=label)
ax.set(xlabel="Transverse hit position x (mm)", ylabel="Counts per bin", title="Synthetic transverse hit-position distributions")
ax.legend()
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(FIGURES / "synthetic_hit_histograms.png", dpi=180)
plt.close(fig)

labels = ["No-target reference", "Aluminium foil"]
means = [results[c]["mean"] for c in conditions]
errors = [results[c]["sem"] for c in conditions]
fig, ax = plt.subplots(figsize=(8, 4.8))
positions = np.arange(len(labels))
ax.errorbar(means, positions, xerr=errors, fmt="o", capsize=5)
ax.axvline(0, linestyle="--", linewidth=1)
ax.set_yticks(positions, labels)
ax.set(xlabel="Mean transverse hit position x (mm)", title="Synthetic sample: mean ± standard error")
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
fig.savefig(FIGURES / "synthetic_mean_errorbars.png", dpi=180)
plt.close(fig)
print("Wrote summary CSV and two PNG figures. Synthetic demonstration only.")
