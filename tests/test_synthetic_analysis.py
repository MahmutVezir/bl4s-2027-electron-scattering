import csv
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/synthetic/example_hits.csv"
SUMMARY = ROOT / "data/synthetic/summary.csv"


class SyntheticDatasetTests(unittest.TestCase):
    def test_dataset_has_two_conditions_and_480_rows(self):
        with DATA.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 480)
        self.assertEqual(
            {row["condition"] for row in rows},
            {"reference_no_target", "aluminium_foil"},
        )

    def test_all_values_are_finite(self):
        with DATA.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                self.assertTrue(math.isfinite(float(row["x_mm"])))

    def test_summary_contains_sample_statistics(self):
        with SUMMARY.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 2)
        for row in rows:
            self.assertEqual(int(row["n"]), 240)
            self.assertGreater(float(row["sample_std_mm"]), 0)
            self.assertGreater(float(row["standard_error_mm"]), 0)

    def test_foil_sample_is_wider_than_reference_in_this_seeded_sample(self):
        with SUMMARY.open(newline="", encoding="utf-8") as handle:
            rows = {r["condition"]: r for r in csv.DictReader(handle)}
        self.assertGreater(
            float(rows["aluminium_foil"]["sample_std_mm"]),
            float(rows["reference_no_target"]["sample_std_mm"]),
        )


if __name__ == "__main__":
    unittest.main()
