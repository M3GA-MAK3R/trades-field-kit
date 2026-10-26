"""Shared pressure-temperature data and bounded linear interpolation.

R410A values: Honeywell Genetron AZ-20 pressure-based PT chart,
3193 | G525-093 | v5 | February 2019, PSIG and degrees Fahrenheit.
Source: https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-genetron-aZ20-pressure-temp-chart-tech-tool1.pdf

Honeywell publishes one temperature column for both calculations in this
R410A chart. Do not reuse this curve for other refrigerants or blends.
Interpolated results are estimates, not manufacturer charging targets.
"""

import argparse
from bisect import bisect_left
import math


R410A_SOURCE_URL = (
    "https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/"
    "en-us/refrigerants/documents/"
    "pmt-am-genetron-aZ20-pressure-temp-chart-tech-tool1.pdf"
)

# Explicit pressure keys preserve the manufacturer's units and chart entries.
SAT_TEMP_R410A = {
    10: -41.1, 15: -33.7, 20: -27.2, 25: -21.4, 30: -16.1,
    35: -11.3, 40: -6.8, 45: -2.6, 50: 1.3, 55: 5.0,
    60: 8.5, 65: 11.8, 70: 14.9, 75: 18.0, 80: 20.9,
    85: 23.6, 90: 26.3, 95: 28.9, 100: 31.4, 105: 33.8,
    110: 36.1, 115: 38.4, 120: 40.6, 125: 42.8, 130: 44.9,
    135: 46.9, 140: 48.9, 145: 50.8, 150: 52.7, 155: 54.5,
    160: 56.4, 165: 58.1, 170: 59.9, 175: 61.6, 180: 63.2,
    185: 64.8, 190: 66.5, 195: 68.0, 200: 69.6, 205: 71.1,
    210: 72.6, 215: 74.0, 220: 75.5, 225: 76.9, 230: 78.3,
    235: 79.7, 240: 81.0, 245: 82.4, 250: 83.7, 255: 85.0,
    260: 86.3, 265: 87.5, 270: 88.8, 275: 90.0, 280: 91.2,
    285: 92.4, 290: 93.6, 295: 94.8, 300: 95.9, 305: 97.1,
    310: 98.2, 315: 99.3, 320: 100.4, 325: 101.5, 330: 102.6,
    335: 103.7, 340: 104.7, 345: 105.8, 350: 106.8, 355: 107.8,
    360: 108.8, 365: 109.8, 370: 110.8, 375: 111.8, 380: 112.8,
    385: 113.7, 390: 114.7, 395: 115.6, 400: 116.6, 405: 117.5,
    410: 118.4, 415: 119.3, 420: 120.2, 425: 121.1, 430: 122.0,
    435: 122.9, 440: 123.7, 445: 124.6, 450: 125.4, 455: 126.3,
    460: 127.1, 465: 128.0, 470: 128.8, 475: 129.6, 480: 130.4,
    485: 131.2, 490: 132.0, 495: 132.8, 500: 133.6, 505: 134.4,
    510: 135.2, 515: 135.9, 520: 136.7, 525: 137.5, 530: 138.2,
    535: 139.0, 540: 139.7, 545: 140.4, 550: 141.2, 555: 141.9,
    560: 142.6, 565: 143.3, 570: 144.0, 575: 144.8, 580: 145.5,
    585: 146.1, 590: 146.8, 595: 147.5, 600: 148.2, 605: 148.9,
    610: 149.5, 615: 150.2,
}


def finite_float(value: str) -> float:
    """Argparse converter that refuses NaN and infinity."""
    number = float(value)
    if not math.isfinite(number):
        raise argparse.ArgumentTypeError("value must be finite")
    return number


def interpolate_sat_temp(chart: dict, pressure: float) -> float:
    """Return a chart value or interpolate, never clamp or extrapolate."""
    if not math.isfinite(pressure):
        raise ValueError("Pressure must be finite")
    pressures = sorted(chart)
    if not pressures:
        raise ValueError("No PT data available")
    if not pressures[0] <= pressure <= pressures[-1]:
        raise ValueError(
            f"Pressure {pressure:g} PSIG is outside the supported PT range "
            f"({pressures[0]:g}-{pressures[-1]:g} PSIG); "
            "use the refrigerant manufacturer's chart"
        )
    index = bisect_left(pressures, pressure)
    upper = pressures[index]
    if upper == pressure:
        return chart[upper]
    lower = pressures[index - 1]
    fraction = (pressure - lower) / (upper - lower)
    return chart[lower] + fraction * (chart[upper] - chart[lower])
