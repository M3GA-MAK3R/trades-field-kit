# Contactor & Capacitor Motor Circuit Diagram (Mermaid)

```mermaid
graph TD
    L1[L1: 240V] --> CONTACTOR[Contactor Contacts]
    L2[L2: 240V] --> CONTACTOR
    CONTACTOR -->|When energized| COMP[Compressor]
    CONTACTOR -->|When energized| CFAN[Condenser Fan Motor]
    
    TSTAT[Thermostat Y] -->|24V| FS[Float Switch]
    FS -->|24V| HPS[High Pressure Switch]
    HPS -->|24V| LPS[Low Pressure Switch]
    LPS -->|24V| COIL[Contactor Coil]
    COIL -->|24V return| C_COMMON[Common C]
    
    CAP[Run Capacitor] -->|C terminal| COMP
    CAP -->|HERM terminal| COMP
    CAP -->|FAN terminal| CFAN
    
    style CONTACTOR fill:#DA7101,stroke:#28251D,color:#fff
    style CAP fill:#20808D,stroke:#28251D,color:#fff
    style COIL fill:#A84B2F,stroke:#28251D,color:#fff
```

## Capacitor Terminal Guide

| Terminal | Connects To |
|----------|-----------|
| C (Common) | Line power + run winding |
| HERM | Compressor start/run winding |
| FAN | Condenser fan motor |

## Safety

**Capacitors store energy even when power is off.**
1. Discharge with a 20kΩ resistor across terminals
2. Wait 30 seconds, short terminals again
3. Verify with meter before handling
4. Never short with a screwdriver (can damage cap or cause arc)

## Contactor Testing

| Test | Method | Expected |
|------|--------|----------|
| Coil voltage | Meter across coil terminals | 24V when thermostat calls |
| Coil continuity | Meter ohms across coil | 10-30Ω (varies by model) |
| Contacts (energized) | Meter across closed contacts | ~0V (no voltage drop) |
| Contacts (de-energized) | Meter across open contacts | 240V (full voltage) |
| Visual | Inspect contact faces | No pitting, burning, or debris |

## Capacitor Testing

| Test | Method | Expected |
|------|--------|----------|
| Capacitance | Capacitance meter across terminals | Within ±10% of rated MFD |
| Visual | Inspect top and body | No bulging, leaking, or case damage |
| Short to ground | Ohm meter, terminal to case | Infinite (OL) |
