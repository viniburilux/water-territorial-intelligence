# WTI — GPIW 2026 application narrative

## Problem

Traditional water monitoring often begins with predefined classes, masks or isolated indicators. WTI addresses a different question: **what changed, where did it change, what independent evidence supports the signal, what remains unknown, and what should be investigated next?**

## Technological insight

Water-relevant change can be represented as a territorial state inside general-purpose territorial representations. The architecture does not require a water-specific mask to detect that territory changed; it then uses independent evidence and provenance to keep interpretation bounded.

## Architecture

`Representation → transformation → localization → corroboration → historical investigation → provenance → next action → state update`.

## Existing heritage

WTI composes GhostWorks / TTI / STT / AlphaEarth embeddings / Sentinel-1 and Sentinel-2 context / temporal trajectories / regime discovery / retrieval / TraceFoundry-style investigation state.

## Prior demonstrations underlying WTI

| Case | Demonstrated capability | Repository status |
|---|---|---|
| Sobradinho / São Francisco | Transformation without a water-specific prior | Executable frozen fixture |
| Rio Joanes | Hotspot → sensor → coordinate → visual investigation | Executable frozen fixture |
| São Paulo mangroves | Ecosystem-scale temporal monitoring | Executable aggregate fixture; raw points not included |
| Baía de Todos os Santos | Regional territorial comparison | Executable aggregate fixture; raw embeddings not included |
| Aral Sea | Water as trajectory | Executable aggregate fixture; raw state vectors not included |

These are prior demonstrations underlying WTI, not five end-to-end field deployments.

## Current stage

The underlying capabilities have been demonstrated separately on real territorial data. This repository is the architectural consolidation and executable proof-of-composition using frozen, provenance-bearing observations.

## Next development

Automate the full chain from territorial source outputs to WTI observations and validate prioritization with field or operational partners.

## Non-claims

WTI does not currently claim real-time water-quality measurement, groundwater chemistry inference, causal attribution, field sensor deployment, autonomous water-management decisions or operational TRL 6–7 maturity.
