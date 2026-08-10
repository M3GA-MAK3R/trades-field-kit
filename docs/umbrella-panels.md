# Handy Helper Umbrella — 8-Panel Field Reference

Each "flap" of the umbrella is a self-contained reference panel. Print, fold, and keep in your truck or tool bag. When you're stuck on a service call, glance at the relevant flap.

---

## Flap 1: Safety First

### Lockout/Tagout (LOTO)
1. **Notify** — inform anyone affected
2. **Shut down** — turn equipment off by normal means
3. **Isolate** — disconnect/break the energy source
4. **Lock out** — apply individual lock + tag to the disconnect
5. **Verify de-energized** — test with a meter (test meter on known source first)
6. **Release** — remove locks/tags only by the person who applied them

### Wet-Work Precautions (Pressure Washing Near Equipment)
- Never pressure wash energized electrical components
- Cover condenser fan motors, contactors, and control boards
- Keep water stream away from electrical disconnects and panels
- Allow equipment to dry completely before re-energizing
- Use GFCI-protected power sources for all tools

### PPE Checklist
- Safety glasses or face shield
- Electrical-rated gloves (Class 0 for up to 1000V)
- Hearing protection
- Closed-toe boots (EH-rated)
- Long pants and sleeves for brazing

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

| Superheat | Likely Cause |
|-----------|-------------|
| Too high (>15-20°F) | Undercharged, restricted metering device, low airflow |
| Too low (<5-10°F) | Overcharged, metering device overfeeding, high airflow |
| Normal (varies by system) | Target varies by indoor/outdoor conditions and manufacturer chart — fixed orifice targets differ from TXV. Always check manufacturer specs. |

### Subcooling (Condenser Performance)
**Formula:** Subcooling = Saturated Liquid Temp − Liquid Line Temp

| Subcooling | Likely Cause |
|------------|-------------|
| Too high (>15-20°F) | Overcharged, restricted liquid line |
| Too low (<5-10°F) | Undercharged, condenser airflow issue |
| Normal (8-12°F) | System operating correctly |

### Quick Check Steps
1. Measure suction/liquid line temperature at the unit
2. Read suction/head pressure gauges
3. Convert pressures to saturated temps using PT chart for your refrigerant
4. Calculate superheat/subcooling
5. Compare to manufacturer specs

---

## Flap 4: Thermostat Low-Voltage Wiring

### Standard Terminal Colors
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
- **Test:** Listen for click, measure voltage across coil (24V), check continuity across contacts (closed when energized)

### Capacitor
| Terminal | Connects To |
|----------|-----------|
| C (Common) | Run winding + power |
| FAN | Condenser fan motor |
| HERM | Compressor |

**WARNING:** Capacitors hold a charge. Always discharge through a resistor before handling.

### Capacitor Testing
1. **Visual:** Bulging or leaking = replace immediately
2. **Discharge:** Use a 20kΩ resistor across terminals
3. **Measure:** With capacitance meter, compare to rated MFD (±10% acceptable)
4. **Start cap:** Check for open circuit if hard-starting

### Common Motor Symptoms
| Symptom | Check |
|---------|-------|
| Motor hums, won't start | Capacitor, bearings, start winding |
- | Contactor not pulling in |
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
   └─ Yes → Check suction/head pressure
      ├─ Low suction, low head → Low charge / leak
      ├─ High suction, high head → Restricted airflow / overcharge
      ├─ Low suction, high head → Restriction (filter drier, metering device)
      └─ High suction, low head → Bad compressor valves
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

### Pressure Washing Maintenance Checklist
- [ ] Cover all electrical components
- [ ] Use low pressure with wide-fan nozzle; prefer garden-hose pressure when possible
- [ ] Spray top-down on condenser, bottom-up is OK for evaporator
- [ ] Use manufacturer-approved coil cleaner; follow label instructions
- [ ] Rinse thoroughly
- [ ] Allow to dry before re-energizing
- [ ] Check coil fins — straighten with fin comb if bent
- [ ] Verify drain is clear after cleaning
