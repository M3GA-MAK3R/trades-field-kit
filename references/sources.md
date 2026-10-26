# References & Sources

## HVAC Training & Education

1. **Anthony's Cool School HVAC Training**
   - https://hvac.anthonyscoolschool.com/
   - Hands-on HVAC training program covering refrigeration cycle, electrical systems, brazing, evacuation, EPA certification, superheat/subcooling, thermostat operations, ductwork, heat pumps, and more.

2. **HVAC School (hvacrschool.com)**
   - https://www.hvacrschool.com/
   - Practitioner-focused HVAC/R training articles, videos, and podcasts. Low-voltage wiring guides, refrigeration cycle explanations, superheat/subcooling methodology.

3. **ACHR News (achrnews.com)**
   - https://www.achrnews.com/
   - Industry news, technical articles, and troubleshooting guides for HVACR professionals.

## Electrical Safety

4. **OSHA — Control of Hazardous Energy (Lockout/Tagout)**
   - https://www.osha.gov/control-hazardous-energy
   - 29 CFR 1910.147 — federal standard for lockout/tagout procedures.

5. **OSHA — Electrical Safety**
   - https://www.osha.gov/electrical
   - General electrical safety standards and guidance.

## Electrical Codes & References

6. **NFPA 70 (National Electrical Code)**
   - https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=70
   - NEC — always verify wire sizing, ampacity, and installation methods against current code edition and local AHJ requirements.

## Refrigerant & PT Chart References

### R410A Calculator Data

The shared table in `calculators/pt_data.py` is transcribed from
[Honeywell's Genetron AZ-20 (R410A) pressure-based PT chart](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-genetron-aZ20-pressure-temp-chart-tech-tool1.pdf),
document 3193 / G525-093, v5, February 2019. The chart gives temperature in
degrees Fahrenheit at gauge pressure in PSIG, with 5-PSIG intervals from
10 through 615 PSIG. Honeywell uses its single temperature column in both the
superheat and subcooling examples.

Both calculators share these values and linearly interpolate between entries.
They reject pressures outside the table, rather than clamping or extrapolating.
Anchor checks include 120 PSIG = 40.6°F, 200 PSIG = 69.6°F,
340 PSIG = 104.7°F, and 430 PSIG = 122.0°F from the linked chart.
The printable reference's pressure conversions use the same shared table.
These are pressure-temperature conversions, not operating or charging targets.

R22 and R134A tables are legacy approximations retained for compatibility; their
values were not revalidated in this correction. Do not treat the R410A regression
tests as verification of those tables or the other calculators. Unlisted
refrigerants, including R32 and R454B, are unsupported; never substitute this
R410A curve. Consult current refrigerant and equipment manufacturer documentation.

### General References

7. **EPA Section 608 Certification**
   - https://www.epa.gov/section608
   - Required for handling refrigerants. Technicians must be certified.

8. **ASHRAE Standards**
   - https://www.ashrae.org/
   - Standards for HVAC system design, ventilation, and energy efficiency.

## Disclaimer

All technical values (pressures, temperatures, wire sizes, ampacities) in this toolkit are approximate references for educational purposes. Always verify against:
- Manufacturer specifications and service manuals
- Current NEC edition and local code amendments
- OSHA regulations for your jurisdiction
- Refrigerant manufacturer PT charts

This toolkit does not replace manufacturer documentation, code books, or professional judgment.
