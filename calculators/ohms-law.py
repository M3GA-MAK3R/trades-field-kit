#!/usr/bin/env python3
"""Ohm's Law calculator for electrical field work.

V = I × R    P = V × I    P = I² × R    P = V² ÷ R
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Ohm's Law calculator. Provide any two values to solve for the rest."
    )
    parser.add_argument("--volts", type=float, help="Voltage (V)")
    parser.add_argument("--amps", type=float, help="Current (A)")
    parser.add_argument("--ohms", type=float, help="Resistance (Ω)")
    parser.add_argument("--watts", type=float, help="Power (W)")
    args = parser.parse_args()

    v = args.volts
    i = args.amps
    r = args.ohms
    p = args.watts

    provided = sum(x is not None for x in [v, i, r, p])
    if provided < 2:
        print("Error: Provide at least two values (--volts, --amps, --ohms, --watts)")
        sys.exit(1)

    # Solve for missing values
    if v is None and i is not None and r is not None:
        v = i * r
    elif v is None and i is not None and p is not None:
        v = p / i
    elif v is None and r is not None and p is not None:
        v = (p * r) ** 0.5

    if i is None and v is not None and r is not None:
        i = v / r
    elif i is None and v is not None and p is not None:
        i = p / v
    elif i is None and r is not None and p is not None:
        i = (p / r) ** 0.5

    if r is None and v is not None and i is not None:
        r = v / i
    elif r is None and v is not None and p is not None:
        r = v ** 2 / p
    elif r is None and i is not None and p is not None:
        r = p / i ** 2

    if p is None and v is not None and i is not None:
        p = v * i
    elif p is None and i is not None and r is not None:
        p = i ** 2 * r
    elif p is None and v is not None and r is not None:
        p = v ** 2 / r

    print(f"\n{'='*40}")
    print(f"  OHM'S LAW CALCULATION")
    print(f"{'='*40}")
    print(f"  Voltage (V):     {v:.2f} V")
    print(f"  Current (I):     {i:.2f} A")
    print(f"  Resistance (R):   {r:.2f} Ω")
    print(f"  Power (P):       {p:.2f} W")
    print(f"{'='*40}")

    # Three-phase estimate
    if v and i:
        p3 = v * i * 1.732 * 0.9
        print(f"  3-phase estimate: {p3:.0f} W (at PF=0.9)")
    print()


if __name__ == "__main__":
    main()
