# WTI capability horizon

The five frozen cases are **evidence anchors, not the boundary of WTI**. This document maps the broader capability substrate visible in the existing corpus and gives each capability the correct evidentiary status.

## Capability map

| Capability | Corpus anchor | WTI status | Meaning |
|---|---|---|---|
| Semantic territorial representation | AlphaEarth / GhostWorks / TTI | Demonstrated capability | 64-dimensional territorial embeddings are used as a general representation of place and time. |
| Transformation measurement | TTI/STT repositories and Sobradinho | Demonstrated capability | TTI/STT measures change between territorial representations without requiring a water-specific mask. |
| Temporal trajectories and annual deltas | GhostWorks serializer and trajectory outputs | Demonstrated capability | The corpus contains temporal summaries, relative deltas, trend and peak-period logic. |
| Anomaly and hotspot discovery | GhostWorks environmental and industrial cases | Demonstrated capability | Outlier summaries and hotspot/candidate ranking turn a broad territory into a priority queue. |
| Clustering and regime discovery | UMAP/HDBSCAN and GhostWorks cluster summaries | Demonstrated capability | Territories can be grouped by behavioral signature rather than geography alone. |
| Analogous-region retrieval | GhostWorks serializer and similar-region outputs | Demonstrated capability | Similar regions can be retrieved in embedding space for comparison and investigation. |
| Multimodal corroboration | Sentinel-1, Sentinel-2, VIIRS and environmental dossiers | Demonstrated capability | Independent signals are used to support, qualify or contradict a territorial signal. |
| Coordinate-linked historical investigation | Rio Joanes and GhostWorks visual materials | Demonstrated capability | A ranked signal can be followed to a coordinate and historical before/after evidence. |
| Structured interpretation | GhostWorks serializer and agent-oriented prompt | Demonstrated capability | Structured territorial outputs can be serialized for human or machine-assisted interpretation. |
| Evidence, claims and gaps | TraceFoundry contracts | Demonstrated capability | Evidence, claims, epistemic status and unresolved gaps are represented explicitly. |
| Research Moves and state updates | TraceFoundry / WTI adapter | Compositional / architectural capability | WTI composes evidence gaps into a proposed next investigative action and state transition. |
| ASIE adaptive investigation pattern | Existing ASIE archaeology and public contract subset | Transferable capability | Frontier → next move → observation → update is a reusable investigation pattern; water integration is not yet a live autonomous loop. |
| Cross-domain territorial intelligence | Mining, mangrove, industrial, Cerrado and Aral materials | Transferable capability | The same representation, retrieval, temporal and investigation mechanisms have been reapplied to distinct territorial questions. |
| Water-specific ontology and operational integration | WTI fixtures and current adapter | Compositional / architectural capability | Water context, provenance and next-action contracts are now composed in frozen offline form. |
| Live sensor fusion, field validation and operational deployment | Not established by current corpus | Future validation | These require new data, partners, repeated operation and independent validation. |

## The progression

```text
EXISTING TERRITORIAL CAPABILITIES
                ↓
WTI COMPOSITION
                ↓
NEW WATER TERRITORIES / EVIDENCE SOURCES
                ↓
AUTOMATED INVESTIGATION
                ↓
FIELD VALIDATION
                ↓
OPERATIONAL WATER INTELLIGENCE
```

The distinction is deliberate. WTI should not be reduced to its smallest reproducible fixture, but neither should transferable or compositional capability be described as field-validated water deployment.

## Corpus anchors

- `viniburilux/TTI_Brazil_2017_2024`: TTI definition, AlphaEarth embeddings, national aggregation, Sobradinho/Remanso case and independent sensor validation.
- `viniburilux/ghostworks`: serializer functions for trajectories, annual deltas, outliers, clusters and similar regions; coordinate-linked case materials; environmental and industrial investigations; agent-oriented structured interpretation.
- WTI `schemas/` and `src/`: evidence-preserving observation, investigation state and Research Move contracts.
- ASIE/TraceFoundry lineage: adaptive investigation and provenance patterns reused in the public WTI composition.

## Boundary

This horizon does not add new empirical claims to the Evidence Register. It makes explicit how demonstrated mechanisms can be transferred and composed, while preserving future validation as a separate category.
