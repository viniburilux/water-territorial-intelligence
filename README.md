# WTI - Water Territorial Intelligence

> **Water Territorial Intelligence is an architecture for turning territorial change into traceable water intelligence: from general territorial representation, through transformation detection, localization and independent corroboration, to evidence, provenance and the next investigative action.**

The five frozen cases are **evidence anchors, not the boundary of the technology**. WTI composes a broader substrate already developed across semantic territorial representation, temporal analysis, anomaly and hotspot discovery, regime discovery, analogous-region retrieval, multimodal corroboration, coordinate-linked investigation, structured interpretation and adaptive evidence workflows.

## Technology Heritage and Composition

WTI was not built from scratch for this repository. It is a **composition architecture**: it composes technological capabilities previously developed and demonstrated across territorial experiments into a water-domain investigation layer.

WTI does not replace the territorial sensing systems that produced its observations. It composes them.

| Layer | Technology / heritage | Role in WTI | Status |
|---|---|---|---|
| Territorial representation | AlphaEarth embeddings / GhostWorks / TTI | Represent territorial state | A |
| Transformation detection | TTI / STT | Detect and quantify territorial transformation without a water-specific mask | A |
| Temporal reasoning | GhostWorks trajectories and annual deltas | Track change through time | A |
| Spatial discovery | GhostWorks hotspots, clustering, regime discovery, analogous-region retrieval | Prioritize locations and transformation regimes | A |
| Independent corroboration | Sentinel-1 SAR and Sentinel-2 NDVI (public executed corroboration); VIIRS and MapBiomas (internal mangrove dossier E-MAN-01) | Provide independent environmental signals | A |
| Water-domain investigation | WTI (this repository) | Convert observations into water investigative states | A (frozen proof-of-composition) |
| Evidence and provenance | TraceFoundry lineage | Preserve evidence, claims, gaps and provenance | A (contracts); D (automated upstream feed) |
| Adaptive investigation | ASIE / investigation-machine lineage | Select the next investigative action from the current frontier | B; C in the water domain |

Status levels: **A - demonstrated** in existing artifacts; **B - composable / transferable** from related systems; **C - architectural capability**, explicit in the system design; **D - next validation**, an integration or validation still to be executed. The full corpus-backed map is maintained in [`docs/capability-horizon.md`](docs/capability-horizon.md).

### The role of GhostWorks / TTI

The current public implementation uses frozen observations derived from previous GhostWorks/TTI experiments to demonstrate the WTI investigation layer.

GhostWorks/TTI is an upstream territorial observation substrate, including capabilities such as semantic territorial representation, satellite-derived embeddings, transformation measurement, temporal trajectories, hotspot discovery, regime/state analysis and spatial retrieval/prioritization.

WTI does not re-implement that substrate inside this repository, and this repository does not execute the full GhostWorks pipeline. WTI composes those observations with water-domain investigation logic.

## Run it first

```bash
python3 demo/run_demo.py
```

The offline demo processes five frozen observations and writes `investigation_state.json` and `research_move.json` under `demo/outputs/`. No network, LLM, GEE or live sensor is required.

The first two cases are coordinate-level demonstrations; the remaining three are executable aggregate fixtures preserving documented evidence without fabricating raw points or coordinates.

Run the test suite (the only dependency is `jsonschema`, used for schema validation):

```bash
pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
```

## The composition map

```text
                    WATER TERRITORY
                           |
                           v
             TERRITORIAL REPRESENTATION        <- AlphaEarth / GhostWorks / TTI
                           |
                           v
                TRANSFORMATION SIGNAL          <- TTI / STT
                           |
          +------------------------------+
          | trajectory / hotspot /       |   <- GhostWorks temporal and spatial discovery
          | regime / state discovery     |
          +------------------------------+
                           |
                           v
             INDEPENDENT CORROBORATION         <- Sentinel-1 SAR / Sentinel-2 NDVI / VIIRS / other layers
                           |
                           v
              LOCATION + INVESTIGATION         <- coordinate-linked historical investigation
                           |
                           v
                 EVIDENCE / PROVENANCE         <- TraceFoundry lineage
                           |
                           v
                 INVESTIGATION STATE           <- WTI
                           |
                           v
             NEXT INVESTIGATIVE ACTION         <- WTI / ASIE adaptive-investigation pattern
                           |
                           +----- state update (iterative investigation cycle)
```

## What WTI adds

The differential of WTI is not "using satellites for water". Existing sensing systems already produce territorial observations. WTI adds the composition layer that turns those observations into investigations:

- transforms territorial signals into investigable objects, with location, time window and source;
- connects transformation signals to independent corroborating evidence;
- preserves provenance behind every claim;
- represents gaps and unknowns explicitly instead of hiding them;
- maintains a reviewable investigation state;
- produces a next investigative action with stop criteria;
- supports iterative investigation cycles.

The central idea: **observation is not the endpoint; observation becomes an investigation state.**

## Current implementation

The current public repository implements the WTI composition layer using five frozen observations derived from previous experiments. The fixtures are intentionally frozen so that the public repository is deterministic and reproducible offline.

The upstream satellite and embedding pipelines are not duplicated inside this repository. That is an architecture and reproducibility decision for the current public proof-of-composition, not a structural limitation of WTI: the five fixtures are the current public implementation of the composition layer; they do not define the full capability space of the architecture.

## Five prior demonstrations

- **Sobradinho / São Francisco:** transformation from general territorial representation without a water-specific mask; 29/36 candidates had at least one independent sensor agreement.
- **Rio Joanes:** hotspot P03 (internal GhostWorks-ESG record) → coordinate and qualitative finding (public GhostWorks) → SAR/NDVI signal (internal record) → historical visual investigation.
- **São Paulo mangroves:** multi-source ecosystem-scale temporal intelligence across approximately 4,000 points and nine coastal municipalities.
- **Baía de Todos os Santos:** regional comparison across eight territories and 33,600 64-dimensional embeddings.
- **Aral Sea:** water represented as states and transitions across a 2018–2024 trajectory.

These are prior demonstrations underlying WTI, not five end-to-end field deployments. Each case demonstrates a different part of the technological space that WTI composes.

## Next integration

The next technological step is to close the chain end to end:

```text
RAW TERRITORIAL DATA
        |
        v
  GhostWorks / TTI          (upstream observation substrate)
        |
        v
TRANSFORMATION OBSERVATION
        |
        v
       WTI  ->  CORROBORATION  ->  EVIDENCE  ->  INVESTIGATION STATE  ->  NEXT ACTION
```

Planned validations, none of them executed yet:

- direct integration with upstream GhostWorks/TTI outputs;
- recovery of raw and point-level artifacts where redistribution is permitted;
- automated execution of the full chain;
- investigative prioritization benchmarks;
- validation with operational partners and field data;
- continuous operationalization.

## Related technology

Public repositories behind the WTI substrate:

- [GhostWorks](https://github.com/viniburilux/ghostworks) - territorial observation substrate: embeddings, transformation measurement, trajectories, hotspot discovery, retrieval and structured serialization.
- [TTI_Brazil_2017_2024](https://github.com/viniburilux/TTI_Brazil_2017_2024) - the Territorial Transformation Index applied to Brazil, including the Sobradinho/São Francisco case and its independent sensor validation.
- [TraceFoundry](https://github.com/viniburilux/TraceFoundry) - evidence, claim, gap, investigation-state and Research Move contracts.
- [GhostWorks Atlas](https://github.com/viniburilux/ghostworks-atlas) - state/transition territorial trajectories, the source of the Aral Sea case.

ASIE (adaptive investigation) belongs to the investigation-machine lineage and is not yet exposed as a standalone public repository; the public TraceFoundry contracts expose the subset reused here.

These repositories are linked, not incorporated: the WTI demo runs without cloning any of them.

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
