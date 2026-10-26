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

### R22 Calculator Data

The R22 table uses the R22 column of
[Honeywell's AZ-20 / Genetron R-22 chart](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-genetron-aZ20-genetronr22-pressure-temp-chart-tech-tool1.pdf),
G525-093, copyright 2011. Temperature-based entries at 5°F intervals from
-40 to 150°F are inverted into exact pressure keys, from 0.6 to 381.7 PSIG.
The adjacent AZ-20 column is not R22 data. For example, 68.6 PSIG = 40°F,
195.9 PSIG = 100°F, and 260 PSIG = 120°F in the linked R22 column.

### R134A Calculator Data

The R134A table is Appendix E, Genetron 134a, of
[Honeywell's Solstice N13 / Genetron 134a retrofit guide](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-solstice-n13-commercial-refrigeration-retrofit-tech-guide1.pdf),
1950 FP Ref v7, December 2017. It contains pressure-based entries from
0 to 280 PSIG, corresponding to -14.9 to 154.7°F. Examples: 40 PSIG = 45°F,
100 PSIG = 87.7°F, and 150 PSIG = 111.5°F. These are the pure R134a values,
not Solstice N13 blend values from other appendices in the guide.

All three tables are shared between the two refrigerant calculators, use bounded
linear interpolation, and have manufacturer-anchor regression tests. These tests
do not certify the other calculators or every technical claim in the field kit.
The tables' ranges are lookup limits, not safe operating limits. Unlisted
refrigerants, including R32 and R454B, remain unsupported; never substitute another
curve. Consult current refrigerant/equipment documentation and applicable safety
and qualification requirements.

## Safety Audit References

See the [audit scope, corrections, and remaining limitations](audit-2026-10-26.md).

The [safety boundaries](../docs/SAFETY.md) distinguish discussion aids from
approved procedures and explain where these U.S. general-industry references
apply. Their inclusion is not a compliance certification.

- **Hazardous energy:** [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147):
  stored energy, verification, device removal, group/shift continuity, and scope exclusions.
- **Electrical work practices:** [OSHA 1910.333](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333):
  de-energization, backfeeds, stored electrical energy, qualified work, and return to service.
- **Instruments/environment:** [OSHA 1910.334](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.334):
  qualified electrical testing, inspections, ratings, and conductive-liquid locations.
- **Protection:** [OSHA 1910.335](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.335):
  task-appropriate PPE and protective equipment.
- **Coil-specific example:** [Johnson Controls TMAL bulletin TPM-SI0245](https://docs.johnsoncontrols.com/ductedsystems/api/khub/documents/TUg78wHItRmyi4kpDTod4w/content):
  prohibits pressure washers, chemicals, and hard-tool contact for the covered
  microchannel coils. Do not generalize this into a recipe for other coils.
- **Refrigerant qualification:** [EPA Section 608 requirements](https://www.epa.gov/section608/section-608-technician-certification-requirements)
  and [technician Q&A](https://www.epa.gov/section608/epas-refrigerant-management-program-questions-and-answers-section-608-certified):
  covered activities and conditions for apprentice exceptions.

### General References

7. **EPA Section 608 Certification**
   - https://www.epa.gov/section608
   - Check the applicable certification and task requirements, including conditions
     for any apprentice exception; see the specific EPA references above.

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
