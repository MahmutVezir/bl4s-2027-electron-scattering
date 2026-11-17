"""Optional ROOT/PyROOT histogram example.
Requires a local ROOT installation with PyROOT enabled.
Run: python analysis/pyroot_histogram.py
This script has not yet been executed in the project's environment.
"""
from pathlib import Path
import csv
import ROOT

ROOT.gROOT.SetBatch(True)
ROOT_DIR = Path(__file__).resolve().parents[1]
INPUT = ROOT_DIR / "data/synthetic/example_hits.csv"
OUT_ROOT = ROOT_DIR / "data/synthetic/example_hits.root"
OUT_PNG = ROOT_DIR / "figures/pyroot_histograms.png"
OUT_PNG.parent.mkdir(exist_ok=True)

reference = ROOT.TH1D("h_reference", "Synthetic hit positions; x (mm); Counts", 50, -2.5, 2.5)
foil = ROOT.TH1D("h_aluminium", "Synthetic hit positions; x (mm); Counts", 50, -2.5, 2.5)
reference.Sumw2()
foil.Sumw2()
with INPUT.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        value = float(row["x_mm"])
        if row["condition"] == "reference_no_target":
            reference.Fill(value)
        elif row["condition"] == "aluminium_foil":
            foil.Fill(value)

canvas = ROOT.TCanvas("canvas", "Synthetic hit distributions", 900, 600)
reference.SetLineColor(ROOT.kBlue + 1)
foil.SetLineColor(ROOT.kOrange + 7)
reference.SetLineWidth(2)
foil.SetLineWidth(2)
reference.Draw("HIST")
foil.Draw("HIST SAME")
legend = ROOT.TLegend(0.62, 0.72, 0.88, 0.88)
legend.AddEntry(reference, "No-target reference", "l")
legend.AddEntry(foil, "Aluminium foil (synthetic)", "l")
legend.Draw()
canvas.SaveAs(str(OUT_PNG))
output = ROOT.TFile(str(OUT_ROOT), "RECREATE")
reference.Write()
foil.Write()
output.Close()
print("Wrote ROOT histogram file and PNG canvas. Synthetic data only.")
