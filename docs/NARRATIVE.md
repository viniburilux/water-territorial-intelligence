# WTI — GPIW 2026 Technology Narrative v0.2

## 1. Opening / One-Sentence Thesis
Water Territorial Intelligence (WTI) is an architecture for turning territorial change into traceable water intelligence: it represents territory, detects transformation, localizes where attention should go, cross-checks independent signals, preserves evidence and gaps, and selects the next investigative action.

The five frozen cases in this repository are **evidence anchors, not the boundary of the technology**. They make the composition executable offline. The broader technology heritage behind WTI includes territorial representation, temporal analysis, anomaly and hotspot discovery, regime discovery, analogous-region retrieval, multimodal corroboration, coordinate-linked investigation, structured interpretation and adaptive evidence workflows already developed across environmental and territorial experiments.

## 2. The Problem

Digital water management has largely inherited the logic of remote-sensing classification: define what water looks like, build a mask for it, and monitor whatever falls inside that mask. That logic works when the question is "how much water is there right now" — and breaks down when the question is "what is changing, where, and how do we know." Static masks miss transformation in systems never labeled as water in the first place. Isolated indices produce scores with no path back to a verifiable place and time. And disconnected dashboards leave every signal standing alone, with no way to compose evidence across sensors, scales, or moments. What water intelligence needs is not another index — it is architecture: a way to move from a general representation of territory to a specific, evidenced, investigable claim about a specific place.

## 3. The Technological Insight

Territory does not need to be told what water is in order to detect that it changed. Large-scale geospatial embeddings — learned representations of land and coastline, trained without a water-specific objective — already encode enough structure that a transformation signal computed directly on the embedding space picks up water-relevant change on its own. That single insight is the seed of WTI: treat water as a *territorial state* inside a general representation, not as a separately engineered detection target. Everything else in the architecture exists to take that raw signal and turn it into something an investigator can trust and act on.

## 4. What Was Built

Across a series of experimental projects, a working technology stack was built and run on real satellite data:

- **A territorial transformation engine** (STT/TTI) that measures semantic change directly from AlphaEarth embeddings, with no water mask required.
- **A multi-sensor corroboration layer** that cross-checks high-transformation candidates against Sentinel-1 SAR, Sentinel-2 NDVI, VIIRS nightlights, MapBiomas, Dynamic World, and Global Mangrove Watch.
- **A coordinate-linked visual investigation workflow** that pulls historical before/after imagery for any flagged location.
- **A temporal trajectory model** that represents a territory as a sequence of states and transitions rather than a single snapshot.
- **A regime-discovery layer** (UMAP/HDBSCAN, archetype clustering, analogous-region retrieval) that groups territories by how they behave, not just where they are.
- **A provenance and claim-discipline layer** (TraceFoundry) that keeps evidence, inference, and hypothesis distinct as claims are built.

These capabilities exist at different evidentiary levels. The repository therefore distinguishes direct demonstrations, transferable mechanisms, compositional architecture and future validation instead of collapsing the technology to the smallest runnable fixture. See [`docs/capability-horizon.md`](capability-horizon.md) for the corpus-backed map.

## 5. How the Capability Emerged

This stack was not designed top-down for a water submission. It accumulated, project by project, each one testing a different piece of the same underlying idea: a semantic transformation metric validated against independent sensors at Sobradinho; a hotspot-plus-visual-verification workflow proven on the Joanes River; a multi-source environmental dossier pipeline built for the São Paulo mangrove coast; a regional comparison infrastructure operationalized across eight territories of the Baía de Todos os Santos; a state-trajectory model applied to the Aral Sea. WTI is what appears when you step back and notice that these were never five different tools — they were five tests of one recurring pattern:

```
territorial representation → transformation measurement → temporal reasoning
→ spatial/regime discovery → independent signal corroboration
→ visual investigation → evidence/provenance → next investigative action
```

WTI names that pattern, formalizes it around water, and makes the composition explicit.

## 6. Capability Horizon — Beyond the Five Demonstrations

The five cases establish anchors across a reservoir, river, mangrove coastline, bay system and inland sea. They do not define the maximum territory, sensor combination or investigative workflow that WTI can support. They show where the architecture has already touched water; the underlying substrate shows how it can be extended.

### Demonstrated capability

Capabilities directly evidenced in existing artifacts include AlphaEarth semantic territorial representation; TTI/STT transformation measurement; temporal trajectories and annual deltas; water-relevant transformation at Sobradinho; SAR/NDVI corroboration; coordinate-linked historical investigation at Joanes; multi-source environmental dossiers; regional comparison; state-transition trajectories; structured serialization; and explicit evidence, claim, gap and Research Move contracts.

### Transferable capability

Other experiments demonstrate mechanisms whose architecture is reusable by WTI: hotspot and candidate ranking, retrieval of analogous regions, clustering and regime discovery, early-mover and onset-oriented temporal reading, multimodal contextual probing with SAR, NDVI, VIIRS and related signals, and agent-oriented interpretation of structured territorial outputs. These are transferable capabilities, not claims that every water task has already been field-validated.

### Compositional / architectural capability

WTI adds a water-specific composition: territorial state → transformation → trajectory/hotspot/regime → corroboration → historical investigation → provenance → claim/gap → Research Move → state update. The offline adapter and five fixtures demonstrate this composition from frozen observations. The complete live loop for arbitrary new water territories remains an integration target.

### Future validation

New water territories, raw evidence sources, field observations, operational partners, live sensors and repeated prioritization benchmarks are the next validation layer. They extend and test an existing architecture; they are not evidence that those future capabilities already operate today.

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

## 7. The WTI Architecture

```
TERRITORY
   ↓
AlphaEarth embeddings — no water mask required
   ↓
Territorial Transformation Signal (STT/TTI)
   ↓
   ┌───────────────┬────────────────┬─────────────────┐
   ▼               ▼                ▼
TEMPORAL        SPATIAL          REGIME
TRAJECTORY      HOTSPOT          DISCOVERY
(state →        (candidate       (analogous
 transition)     + coordinate)    territories)
   │               │                │
   └───────┬───────┴────────┬───────┘
           ▼                ▼
   INDEPENDENT SENSOR   HISTORICAL VISUAL
   CORROBORATION        INVESTIGATION
   (SAR · NDVI · VIIRS ·  (coordinate-linked
    MapBiomas · GMW)       before/after imagery)
           │                │
           └───────┬────────┘
                    ▼
        TRACEFOUNDRY PROVENANCE LAYER
        evidence → claim → gap → next action
                    ▼
        AUDITABLE TERRITORIAL INTELLIGENCE
```

The architecture's job is to take a territory, in any water-relevant form — reservoir, river, coastline, bay, inland sea — and carry it through the same pipeline, producing a result that is both a *finding* and a *traceable evidence chain* at the same time.

## 8. Five Experimental Demonstrations

**Sobradinho Reservoir / São Francisco River — signal without a prior.** The transformation engine detected extreme retraction of the Sobradinho reservoir directly from AlphaEarth embeddings, with no water-specific mask involved — the strongest proof that WTI's core signal generalizes to water without being told what water is. Independent Sentinel-1/Sentinel-2 corroboration reached agreement on 80.5% of the highest-signal candidates, and historical imagery confirmed the retraction visually.

**Rio Joanes — hotspot to visual evidence.** Within a five-kilometer territorial scan, the architecture isolated a single river hotspot as the strongest SAR anomaly in the set (+7.19 dB) and, following its own coordinate, retrieved historical imagery from 2019 and 2023 that visibly confirmed a change in the water body. This is the architecture's hotspot-to-verification pipeline running end to end on a real location.

**São Paulo Mangrove Coastline — ecosystem-scale regime intelligence.** Across roughly 4,000 points and seven years, the same engine produced a multi-source temporal dossier — Dynamic World, MapBiomas, Global Mangrove Watch, VIIRS, and four-epoch Sentinel-2 imagery — that distinguished conserved, anthropized, and rapidly-changing mangrove regimes across nine coastal municipalities, with a coordinate-level visual audit trail for the highest-priority points.

**Baía de Todos os Santos — regional territorial comparison.** The pipeline scaled to 33,600 embeddings across eight territories of a full bay system, ranking them by relative transformation intensity on one consistent metric — proof that the architecture composes across an entire region, not just a single site.

**Aral Sea — water as trajectory.** Instead of a single before/after comparison, the Aral Sea was represented as a full sequence of territorial states and transitions across 2018–2024 — demonstrating that the architecture treats water loss as a process with structure, not a one-time snapshot.

## 9. What These Demonstrations Have in Common

Every case runs the same four moves, on a different water system, at a different scale: **a transformation signal computed without a water-specific prior; corroboration against independent physical evidence; a path from signal to a specific, verifiable location; and a way of holding what is known separate from what is inferred.** A reservoir, a river hotspot, a mangrove coastline, a bay, and an inland sea are structurally different water systems — and the same pipeline produced evidence-backed findings on all five. That consistency, not any single case, is the real result.

## 10. What Becomes Possible Through Composition

Individually, each case was a proof of one capability. Composed, they become something categorically different: an architecture that can be pointed at *any* water territory — known or unfamiliar, large or small, sudden or gradual — and produce the same kind of output every time: a located, corroborated, provenance-tracked claim, plus an explicit next investigative question. Composition is what turns five demonstrated capabilities into one deployable intelligence layer.

## 11. Why This Matters for Water

Water systems are exactly the domain where territorial intelligence pays off most: they change on multiple time scales at once (sudden hotspots and slow multi-year trajectories), they cross conventional monitoring boundaries (a river doesn't respect a municipal border, a mangrove doesn't respect a classification scheme), and they are chronically under-instrumented relative to their importance. An architecture that can generalize a transformation signal across reservoirs, rivers, coastlines, bays, and inland seas — using the same underlying representation — is precisely the kind of infrastructure water intelligence has been missing.

## 12. Impact and Application Pathways

- **Environmental risk screening** — surfacing which territories deserve field attention before resources are committed.
- **Water-risk intelligence** for ESG and industrial-adjacent due diligence, with an auditable evidence trail instead of a black-box score.
- **Watershed and coastal-ecosystem monitoring** at scale, distinguishing stable, recovering, and degrading regimes.
- **Infrastructure/environmental risk investigation**, using the hotspot-to-visual-verification pipeline already proven at Joanes.
- **Analogous-regime discovery**, transferring knowledge from well-understood territories to under-monitored ones with similar behavioral signatures.

## 13. Current Development Stage

The core capabilities — transformation detection, multi-sensor corroboration, visual verification, trajectory modeling, regime discovery — are each independently proven on real satellite data across five distinct water systems, with additional transferable mechanisms demonstrated in adjacent territorial and environmental investigations. The unified WTI state schema that composes them into one pipeline exists as a working proof-of-composition artifact, and five frozen observations now run through the offline adapter. The current stage is architectural consolidation: turning a broader territorial-intelligence substrate into a water system that can run the full chain automatically for new territories.

## 14. Next Development Step

The next step is field-anchored validation: pairing the architecture with a real operational partner — an environmental audit, a municipal water authority, a conservation program — to close the loop between computational evidence and ground truth, and to harden the TraceFoundry layer into an automatic output rather than a manually constructed narrative.

## 15. Closing Argument

WTI is not a proposal to build water intelligence from scratch. It is the recognition that a territorial intelligence pattern — proven independently on a reservoir, a river, a mangrove coastline, a bay, and a collapsing sea — already exists, already generalizes, and is ready to be composed into a single architecture purpose-built for water. The technology is larger than any one artifact that formalizes it: it is a demonstrated capability to turn territory, anywhere, into evidence.
