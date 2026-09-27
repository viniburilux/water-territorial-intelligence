# WTI — Water Territorial Intelligence

> **Water Territorial Intelligence is an architecture for turning territorial change into traceable water intelligence: from general territorial representation, through transformation detection, localization and independent corroboration, to evidence, provenance and the next investigative action.**

The five frozen cases are **evidence anchors, not the boundary of the technology**. WTI composes a broader substrate already developed across semantic territorial representation, temporal analysis, anomaly and hotspot discovery, regime discovery, analogous-region retrieval, multimodal corroboration, coordinate-linked investigation, structured interpretation and adaptive evidence workflows.

## Run it first

```bash
python3 demo/run_demo.py
```

The offline demo processes five frozen observations and writes `investigation_state.json` and `research_move.json` under `demo/outputs/`. No network, LLM, GEE or live sensor is required.

The first two cases are coordinate-level demonstrations; the remaining three are executable aggregate fixtures preserving documented evidence without fabricating raw points or coordinates.

## The architecture

```text
WATER TERRITORY
       ↓
TERRITORIAL REPRESENTATION
       ↓
TRANSFORMATION SIGNAL
       ↓
TRAJECTORY · HOTSPOT · REGIME
       ↓
INDEPENDENT CORROBORATION
       ↓
LOCATION + HISTORICAL / VISUAL INVESTIGATION
       ↓
TRACEABLE EVIDENCE
       ↓
CLAIM / GAP
       ↓
NEXT INVESTIGATIVE ACTION
       ↓
STATE UPDATE ↺
```

The technology horizon is larger than the offline fixture runner: existing territorial capabilities → WTI composition → new water territories and evidence sources → automated investigation → field validation → operational water intelligence. See [`docs/capability-horizon.md`](docs/capability-horizon.md).

## Five prior demonstrations

- **Sobradinho / São Francisco:** transformation from general territorial representation without a water-specific mask; 29/36 candidates had at least one independent sensor agreement.
- **Rio Joanes:** hotspot P03 → coordinate → SAR/NDVI signal → historical visual investigation.
- **São Paulo mangroves:** multi-source ecosystem-scale temporal intelligence across approximately 4,000 points and nine coastal municipalities.
- **Baía de Todos os Santos:** regional comparison across eight territories and 33,600 64-dimensional embeddings.
- **Aral Sea:** water represented as states and transitions across a 2018–2024 trajectory.

These are prior demonstrations underlying WTI, not five end-to-end field deployments.

## Repository map

- `demo/` — five executable frozen observations and the offline adapter runner.
- `cases/` — case-level explanations and canonical observation copies.
- `schemas/` — minimal contracts for observations, investigation state and research moves.
- `src/` — deterministic WTI adapter.
- `docs/` — architecture, narrative, capability horizon, evidence register, epistemic discipline, lineage and roadmap.
- `submissions/gpiw-2026/` — GPIW application narrative and evidence map, kept separate from the technical core.

## Epistemic discipline

WTI explicitly represents what evidence establishes, what it suggests, what remains unknown and what should be investigated next. A territorial signal is not automatically a water-level, water-quality, contamination or causal measurement. WTI distinguishes **demonstrated capability**, **transferable capability**, **compositional/architectural capability** and **future validation**. See [`docs/epistemic-discipline.md`](docs/epistemic-discipline.md) and [`docs/capability-horizon.md`](docs/capability-horizon.md).

## What is not claimed

No live IoT water-sensor operation, groundwater chemistry, causal attribution, field validation, deployed users, operational partners or autonomous water-management decisions are claimed by this repository. HydraLux/WaterLux/LuxSense are related lineage or future sensing directions, not primary empirical evidence for WTI; see [`docs/water-domain-lineage.md`](docs/water-domain-lineage.md).

## License

MIT — see [`LICENSE`](LICENSE).
