"""First-order Lynch-Dahl multiple-scattering estimates for aluminium foils.

This is an analytical planning calculator, not a beam simulation and not measured data.
Momentum is in MeV/c, foil thickness in micrometres, and distances in millimetres.
Only the central projected distribution is approximated; non-Gaussian tails,
electron energy-loss effects, beam optics and detector response are not simulated.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from typing import Iterable

ELECTRON_MASS_MEV = 0.51099895
ALUMINIUM_DENSITY_G_CM3 = 2.699
ALUMINIUM_RADIATION_LENGTH_G_CM2 = 24.01
ALUMINIUM_RADIATION_LENGTH_CM = (
    ALUMINIUM_RADIATION_LENGTH_G_CM2 / ALUMINIUM_DENSITY_G_CM3
)


def estimate_projected_scattering(
    momentum_mev_c: float,
    thickness_um: float,
    distance_mm: float,
) -> dict[str, float]:
    """Return a first-order central projected scattering estimate.

    The angular width follows PDG Review of Particle Physics 2025,
    Sec. 34.3, Eq. 34.16 (Lynch-Dahl approximation), for |z| = 1.

    The displacement estimate is distance_mm * theta0 and assumes small angles
    and a thin target compared with the target-to-sensor distance.
    """
    values = (momentum_mev_c, thickness_um, distance_mm)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("All inputs must be finite numbers.")
    if momentum_mev_c <= 0:
        raise ValueError("Momentum must be greater than zero.")
    if thickness_um <= 0:
        raise ValueError("Foil thickness must be greater than zero.")
    if distance_mm < 0:
        raise ValueError("Distance cannot be negative.")

    thickness_cm = thickness_um * 1e-4
    areal_thickness_g_cm2 = (
        ALUMINIUM_DENSITY_G_CM3 * thickness_cm
    )
    x_over_x0 = (
        areal_thickness_g_cm2 / ALUMINIUM_RADIATION_LENGTH_G_CM2
    )

    beta = momentum_mev_c / math.sqrt(
        momentum_mev_c**2 + ELECTRON_MASS_MEV**2
    )
    log_argument = x_over_x0 / beta**2
    correction = 1.0 + 0.038 * math.log(log_argument)

    if correction <= 0:
        raise ValueError(
            "Inputs fall outside the useful range of this approximation."
        )

    theta0_rad = (
        13.6
        / (beta * momentum_mev_c)
        * math.sqrt(x_over_x0)
        * correction
    )
    displacement_mm = distance_mm * theta0_rad

    return {
        "momentum_mev_c": momentum_mev_c,
        "beta": beta,
        "thickness_um": thickness_um,
        "x_over_x0": x_over_x0,
        "theta0_mrad": theta0_rad * 1e3,
        "distance_mm": distance_mm,
        "sigma_displacement_mm": displacement_mm,
        "sigma_displacement_pixels": displacement_mm / 0.055,
    }


def rows_for_scan(
    momenta: Iterable[float],
    thicknesses: Iterable[float],
    distance_mm: float,
) -> list[dict[str, float]]:
    """Build a result table for each momentum/thickness pair."""
    return [
        estimate_projected_scattering(momentum, thickness, distance_mm)
        for thickness in thicknesses
        for momentum in momenta
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Estimate central electron multiple-scattering widths in Al."
    )
    parser.add_argument(
        "--momenta",
        nargs="+",
        type=float,
        default=[60.0, 100.0, 150.0, 220.0],
        help="Momentum values in MeV/c.",
    )
    parser.add_argument(
        "--thicknesses",
        nargs="+",
        type=float,
        default=[100.0, 200.0],
        help="Aluminium foil thickness values in micrometres.",
    )
    parser.add_argument(
        "--distance-mm",
        type=float,
        default=200.0,
        help="Illustrative target-to-sensor distance in millimetres.",
    )
    args = parser.parse_args()

    try:
        rows = rows_for_scan(
            args.momenta,
            args.thicknesses,
            args.distance_mm,
        )
    except ValueError as exc:
        parser.error(str(exc))

    fieldnames = list(rows[0].keys()) if rows else []
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
