# Refrigeration Cycle Diagram (Mermaid)

```mermaid
graph TD
    A[Compressor] -->|High-pressure vapor| B[Condenser]
    B -->|High-pressure liquid| C[Metering Device<br/>TXV/Piston/Cap Tube]
    C -->|Low-pressure liquid+vapor| D[Evaporator]
    D -->|Low-pressure vapor| A
    
    B -.->|Rejects heat to outdoor air| OUT[Outdoor Air]
    D -.->|Absorbs heat from indoor air| IN[Indoor Air]
    
    style A fill:#DA7101,stroke:#28251D,color:#fff
    style B fill:#A84B2F,stroke:#28251D,color:#fff
    style C fill:#20808D,stroke:#28251D,color:#fff
    style D fill:#01696F,stroke:#28251D,color:#fff
```

## Component Details

| Component | Function | Location |
|-----------|----------|----------|
| Compressor | Raises pressure/temp of refrigerant vapor | Outdoor unit |
| Condenser | Rejects heat, vapor → liquid | Outdoor unit |
| Metering Device | Drops pressure, liquid → mixed phase | Indoor unit (TXV) or outdoor (piston) |
| Evaporator | Absorbs heat, liquid → vapor | Indoor unit |

## Pressure/Temperature Zones

- **High side:** Compressor discharge → condenser → metering device inlet
  - R410A: ~350-450 PSI, 100-120°F saturated
- **Low side:** Metering device outlet → evaporator → compressor suction
  - R410A: ~100-140 PSI, 40-55°F saturated

## Common Metering Device Types

1. **TXV (Thermostatic Expansion Valve)** — modulates based on superheat, most efficient
2. **Fixed piston/orifice** — simple, charge-sensitive, common in lower-end units
3. **Capillary tube** — used in small systems (window units, mini-splits)
4. **EEV (Electronic Expansion Valve)** — electronically controlled, variable capacity
