import math
import unittest

from physics.scattering_estimates import (
    ALUMINIUM_RADIATION_LENGTH_CM,
    estimate_projected_scattering,
)


class ScatteringEstimateTests(unittest.TestCase):
    def test_radiation_length_conversion(self):
        self.assertAlmostEqual(
            ALUMINIUM_RADIATION_LENGTH_CM,
            8.8959,
            places=3,
        )

    def test_reference_estimate_is_reproducible(self):
        result = estimate_projected_scattering(
            momentum_mev_c=100.0,
            thickness_um=100.0,
            distance_mm=200.0,
        )
        self.assertAlmostEqual(result["theta0_mrad"], 3.3832, places=3)
        self.assertAlmostEqual(
            result["sigma_displacement_mm"],
            0.6766,
            places=3,
        )

    def test_scattering_decreases_with_momentum(self):
        low = estimate_projected_scattering(60.0, 100.0, 200.0)
        high = estimate_projected_scattering(220.0, 100.0, 200.0)
        self.assertGreater(low["theta0_mrad"], high["theta0_mrad"])

    def test_scattering_increases_with_thickness(self):
        thin = estimate_projected_scattering(100.0, 100.0, 200.0)
        thick = estimate_projected_scattering(100.0, 200.0, 200.0)
        self.assertGreater(thick["theta0_mrad"], thin["theta0_mrad"])

    def test_pixel_scale_conversion(self):
        result = estimate_projected_scattering(100.0, 100.0, 200.0)
        self.assertAlmostEqual(
            result["sigma_displacement_pixels"] * 0.055,
            result["sigma_displacement_mm"],
            places=10,
        )

    def test_invalid_inputs_are_rejected(self):
        for args in [
            (0.0, 100.0, 200.0),
            (100.0, 0.0, 200.0),
            (100.0, 100.0, -1.0),
            (math.nan, 100.0, 200.0),
        ]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    estimate_projected_scattering(*args)


if __name__ == "__main__":
    unittest.main()
