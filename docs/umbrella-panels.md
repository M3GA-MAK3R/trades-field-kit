# Handy Helper Umbrella — 8-Panel Field Reference

Each "flap" of the umbrella is a self-contained reference panel. Print, fold, and keep in your truck or tool bag. When you're stuck on a service call, glance at the relevant flap.

Educational discussion aid, not official paperwork or authorization to work.
Read [Safety and Authorization Boundaries](SAFETY.md) first. Existing operating
readings can be discussed; this reference does not supply live-probing instructions.
Keep actual job records and photos in approved private systems.

---

## Flap 1: Safety First

### Lockout/Tagout (LOTO)
Use the employer's applicable program and equipment-specific procedure, not this
panel as a sequence. Discuss all sources, stored energy, reaccumulation,
authorized roles, isolation verification, group/shift continuity, and stop-work
conditions. A disconnect position or meter reading alone does not verify all
hazards. Use the applicable return-to-service and device-removal procedure; this
aid does not authorize removal of another person's lock.

### Wet-Work Precautions (Pressure Washing Near Equipment)
- Never pressure wash energized electrical components
- Follow equipment instructions for protection of motors, controls, and compartments
- Keep water stream away from electrical disconnects and panels
- Allow equipment to dry completely before re-energizing
- Use electrical tools approved for the location, with required protection
- Covers, GFCIs, and drying do not replace isolation or authorization

### PPE Checklist
Select eye/face, shock/arc, chemical, hearing, foot, and other protection from the
task-specific assessment. No glove class or generic clothing list establishes a
complete protective system. See [OSHA 1910.335](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.335).

---

## Flap 2: Refrigeration Cycle

```
        COMPRESSOR
        ┌─────────┐
   ───► │         │ ───► High-pressure vapor
   Suc.  │         │       to Condenser
   line  └─────────┘
    ▲                     
    │ Low-pressure vapor   
    │ from Evaporator      

    CONDENSER          METERING DEVICE
    ┌──────────┐       ┌──────────────┐
    │ High-P   │ ────► │ Liquid       │ ───► Low-pressure
    │ vapor →  │       │ enters,      │     liquid/vapor
    │ liquid   │       │ drops P      │     to Evaporator
    └──────────┘       └──────────────┘
    
         EVAPORATOR
         ┌──────────┐
         │ Absorbs   │
         │ heat from │
         │ indoor    │
         │ air       │
         └──────────┘
```

**Cycle Summary:**
1. Compressor raises refrigerant pressure and temperature
2. Condenser rejects heat — refrigerant becomes liquid
3. Metering device drops pressure — liquid becomes mixed phase
4. Evaporator absorbs heat — refrigerant becomes vapor
5. Vapor returns to compressor

---

## Flap 3: Superheat & Subcooling

### Superheat (Evaporator Performance)
**Formula:** Superheat = Suction Line Temp − Saturated Suction Temp (from PT chart)

Use the equipment manufacturer's target for its metering device and measured
conditions. Fixed-orifice and regulated-valve systems need their applicable
methods; there is no universal target or one-reading charge diagnosis.

### Subcooling (Condenser Performance)
**Formula:** Subcooling = Saturated Liquid Temp − Liquid Line Temp

Compare with the model-specific target and charging method. A number by itself
does not prove correct operation or authorize an adjustment.

### Quick Check Steps
1. Identify refrigerant, operating mode, metering device, and specification source.
2. Use existing authorized, stable readings with paired pressure/temperature locations.
3. Select the correct refrigerant PT chart and pressure units; use dew/bubble
   values as applicable to the identified blend and calculation.
4. Calculate and compare with the applicable manufacturer method, considering airflow
   and other conditions; do not adjust charge from pressure patterns alone.

See [calculator data and limits](../calculators/README.md).

---

## Flap 4: Thermostat Low-Voltage Wiring

### Standard Terminal Colors
Colors are conventions, not wiring instructions. Verify terminal functions,
voltages, safety circuits, and O/B logic on the exact equipment schematic.

| Terminal | Wire Color | Function |
|----------|-----------|----------|
| R / RH / RC | Red | 24V power (heat / cool) |
| C | Blue (or brown) | Common (24V return) |
| Y / Y1 | Yellow | Cooling (compressor/contactor) |
| G | Green | Fan (blower) |
| W / W1 | White | Heating (heat strips / gas valve) |
| O | Orange | Reversing valve (cool mode, most brands) |
| B | Dark Blue | Reversing valve (heat mode, Ruud/Rheem) |
| W2 | White (2nd) | Auxiliary / 2nd-stage heat |
| Y2 | Yellow (2nd) | 2nd-stage cooling |

### Common Failure Checks
- **No 24V at thermostat** → Check transformer, fuse on control board, float switch
- **Thermostat blank** → Check R-C for 24V, check C wire connection
- **Fan won't stop** → G wire shorted, fan relay stuck, thermostat stuck
- **No cooling** → Y not reaching contactor, check float switch, pressure switches
- **Reversing valve wrong mode** → O/B wiring — verify energize-in-cool vs energize-in-heat

### Float Switch Note
Many techs wire the float switch to break R (kills thermostat + defrost board) or Y (kills cooling only). Know which method was used.

---

## Flap 5: Contactor & Capacitor Motor Circuits

### Contactor
- Coil: 24V from thermostat Y terminal → through safety switches → contactor coil
- Contacts: Line voltage (240V) through contacts to compressor and condenser fan
- **Common failures:** pitted/burned contacts, coil burnout, ants/debris in contactor
- **Assessment:** Use the model schematic and approved isolated-work inspection
  method. A click does not prove safe isolation or healthy contacts; refer required
  energized testing to qualified, authorized personnel.

### Capacitor
| Terminal | Connects To |
|----------|-----------|
| C (Common) | Run winding + power |
| FAN | Condenser fan motor |
| HERM | Compressor |

**WARNING:** Capacitors and drives can retain hazardous energy after disconnection.
Use the manufacturer's discharge, wait, and verification procedure with approved
rated tools. No universal resistor value or waiting period is specified here.

### Capacitor Testing
Only qualified, authorized personnel following the applicable isolation and
stored-energy procedure may inspect/test. Compare capacitance with the component's
marked tolerance and manufacturer instructions, not a generic percentage.
Do not improvise terminal shorting. See [capacitor safety](SAFETY.md#capacitors-drives-and-ppe).

### Common Motor Symptoms
| Symptom | Check |
|---------|-------|
| Motor hums, won't start | Capacitor, bearings, start winding |
| Contactor not pulling in | Approved control-circuit diagnosis by qualified personnel |
| Motor overheats | Bearings, voltage, airflow, capacitor too high |
| Compressor short-cycles | Low/high pressure switch, overload, charge level |

---

## Flap 6: Heat Pump Sequence & Defrost

### Heating Mode Sequence
1. Thermostat calls for heat (W/Y energizes)
2. Reversing valve positions for heating (de-energized on most brands)
3. Compressor starts — outdoor coil becomes evaporator (absorbs heat)
4. Indoor coil becomes condenser (rejects heat)
5. Supplemental heat (W2) engages if needed

### Defrost Cycle
- **When:** Ice builds on outdoor coil (typically below 40°F outdoor)
- **Trigger:** Defrost board timer/thermostat detects frost
- **Action:** Reversing valve switches to cooling mode, outdoor fan stops, heat strips energize
- **Duration:** Usually 5-15 minutes
- **Exit:** Defrost thermostat senses coil temp rise, returns to heating

### Defrost Troubleshooting
| Problem | Check |
|---------|-------|
| Never defrosts | Defrost sensor/board, reversing valve stuck |
| Defrosts too often | Sensor location/accuracy, ambient temp sensor |
| Won't exit defrost | Sensor stuck closed, board relay welded |
| Ice build-up on coil | Low charge, low airflow, defrost failure |

### Reversing Valve Brand Notes
- Most brands: energize O in cooling (de-energized = heating)
- Ruud/Rheem: energize B in heating (de-energized = cooling)

---

## Flap 7: Electrical Pocket Formulas

### Ohm's Law
```
V = I × R    |    I = V ÷ R    |    R = V ÷ I
```
- V = Volts | I = Amps | R = Ohms

### Power
```
P = V × I    |    P = I² × R    |    P = V² ÷ R
```
- P = Watts | Single phase

### Three-Phase Power
```
P = V × I × 1.732 × PF
```
- PF = Power Factor (typically 0.8-0.95)

### Voltage Drop
```
VD = 2 × K × I × D ÷ CM
```
- K = 12.9 (copper resistivity)
- I = Current (amps)
- D = One-way distance (feet)
- CM = Circular mils (from AWG table)

### Common Wire Sizes (Copper)
| AWG | Ampacity (60°C) | CM |
|-----|----------------|-----|
| 14 | 15A | 4,107 |
| 12 | 20A | 6,530 |
| 10 | 30A | 10,380 |
| 8 | 40A | 16,510 |
| 6 | 55A | 26,240 |

**WARNING:** Always verify ampacity against NEC tables and local code. Derating may apply.

### Motor Full-Load Current Quick Estimate
- 240V single-phase: FLA ≈ HP × 4.5
- 208-230V three-phase: FLA ≈ HP × 2.5

---

## Flap 8: Troubleshooting Decision Flow

### No Cooling
```
Thermostat set to COOL and below room temp?
├─ No → Check thermostat, batteries, display
└─ Yes → Is outdoor unit running?
   ├─ No → Check breaker/disconnect → contactor → capacitor → compressor
   └─ Yes → Compare authorized readings, airflow, mode, and load
      ├─ Confirm refrigerant, paired measurements, and stable conditions
      ├─ Compare with the equipment manufacturer's diagnostic method
      └─ Pressure patterns alone do not identify a fault or justify charging
```

### No Heat (Heat Pump)
```
Thermostat set to HEAT and above room temp?
├─ No → Check thermostat
└─ Yes → Is outdoor unit running?
   ├─ No → Breaker, defrost board, reversing valve
   └─ Yes → Aux heat engaging?
      ├─ No → Check heat strips, sequencer, W2 wiring
      └─ Yes → Check refrigerant charge, reversing valve position
```

### Short Cycling
- Check: thermostat location (drafts), filter cleanliness, coil freeze-up, low charge, oversized equipment, pressure switch tripping

### Coil Cleaning Discussion
Read the exact coil instructions before choosing chemicals, pressure, distance,
spray direction, or fin tools. Do not assume a pressure washer is permitted;
some microchannel instructions prohibit both pressure washers and chemicals.
Use the [wet-work discussion checklist](field-checklists/pressure-washing.md)
and approved return-to-service process, not a generic spray recipe.
