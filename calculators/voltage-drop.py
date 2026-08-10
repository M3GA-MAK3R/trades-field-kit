#!/usr/bin/env python3
"""Voltage drop calculator for electrical field work.

VD = 2 × K × I × D ÷ CM
"""

import argparse

# AWG to Circular Mils table (copper)
AWG_CM = {
    18: 1620, 16: 2580, 14: 4107, 12: 6530, 10: 10380,
    8: 16510, 6: 26240, 4: 41740, 2: 66360, 1: 83690,
    "1/0": 105600, "2/0": 133100, "3/0": 167800, "4/0": 211600,
}

K_COPPER = 12.9  # resistivity at 75°C


def main():
    parser = argparse.ArgumentParser(description="Calculate voltage drop in copper conductors")
    parser.add_argument("--amps", type=float, required=True, help="Current (A)")
    parser.add_argument("--length", type=float, required=True,
                        help="One-way circuit length (ft)")
    parser.add_argument("--wire-gauge", type=str, required=True,
                        help="Wire gauge (e.g., 12, 10, 8, 4, 2/0)")
    parser.add_argument("--voltage", type=float, default=240,
                        help="Supply voltage (V)")
    args = parser.parse_args()

    gauge = args.wire_gauge
    try:
        gauge_key = int(gauge)
    except ValueError:
        gauge_key = gauge

    if gauge_key not in AWG_CM:
        print(f"Error: Unknown wire gauge '{gauge}'. Available: {list(AWG_CM.keys())}")
        return

    cm = AWG_CM[gauge_key]
    vd = 2 * K_COPPER * args.amps * args.length / cm
    vd_percent = (vd / args.voltage) * 100

    print(f"\n{'='*45}")
    print(f"  VOLTAGE DROP CALCULATION")
    print(f"{'='*45}")
    print(f"  Wire gauge:    {gauge} AWG ({cm:,} CM)")
    print(f"  Current:       {args.amps} A")
    print(f"  One-way length: {args.length} ft")
    print(f"  Supply voltage: {args.voltage} V")
    print(f"{'='*45}")
    print(f"  Voltage drop:   {vd:.2f} V")
    print(f"  Drop %:        {vd_percent:.2f}%")
    print(f"{'='*45}")

    if vd_percent > 5:
        print("  ⚠  EXCEEDS 5% — NEC recommended max. Increase wire size.")
    elif vd_percent > 3:
        print("  →  Above 3% — consider upsizing for efficiency")
    else:
        print("  ✓  Within acceptable range (<3%)")
    print()

    print("  NOTE: Values for copper at 75°C. Verify against NEC")
    print("  Article 310 and local code for final determination.")


if __name__ == "__main__":
    main()
