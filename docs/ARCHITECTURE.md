# GPIW Water Intelligence Architecture

**Working object:** Water Territorial Intelligence (WTI)
**Date:** 2026-09-26
**Purpose:** compose existing LuxVerso technology into a demonstrable water-intelligence system for GPIW 2026.

---

## 1. Executive finding

The strongest existing technology is **not** the legacy HydraLux/WaterLux proposal by itself.

The strongest evidence-backed composition already present in the patrimony is:

> **Satellite semantic representation + temporal territorial change detection + independent environmental signals + spatial retrieval/prioritization + evidence/provenance + investigation state + next-action selection.**

In practical terms:

**GhostWorks / TTI** supplies the territorial sensing and change-detection substrate.
**Sentinel/SAR/NDVI/VIIRS evidence** supplies independent environmental interpretation.
**TraceFoundry** supplies explicit evidence, provenance, claims, gaps and reviewable investigation state.
**ASIE** supplies the adaptive-investigation pattern: the system does not end at an alert; the current frontier determines the next research move.
**Existing agent/serializer work** supplies the bridge from structured territorial outputs to machine-assisted interpretation.

The water-specific proof is already present in the patrimony:

1. The TTI Brazil repository documents a **Remanso/BA case on the São Francisco River** where TTI captured strong water-body retraction without a dedicated water mask: mean TTI 0.133, 3.1× national mean, maximum 0.690.
2. The same repository records independent Sentinel-2 NDVI + SAR validation: **80.5% of 36 candidate points showed at least one independent sensor confirming transformation**.
3. GhostWorks-ESG documents a **SAR anomaly of +7.19 dB near the Joanes River**, interpreted in the paper as indicative of significant physical alteration of a water body, with coordinate/date-verifiable satellite evidence.
4. GhostWorks already has temporal trajectories, annual deltas, anomaly detection, clustering, similar-region retrieval and an agent-oriented serializer.
5. TraceFoundry already has versioned evidence references, claims with epistemic status, explicit gaps, investigation state and Research Moves with stop criteria.

The missing innovation is therefore **composition and water-specific operationalization**, not invention of a new foundation model.

The five frozen WTI cases are evidence anchors, not the capability boundary. The broader corpus supports four distinct levels: **demonstrated capability** where an existing artifact directly shows the mechanism; **transferable capability** where the mechanism was demonstrated in another territorial or environmental context; **compositional/architectural capability** where WTI combines those mechanisms into a water-specific contract; and **future validation** where new field data, partners or deployment are still required. The public map is maintained in [`docs/capability-horizon.md`](capability-horizon.md).

---

## 2. Problem being attacked

### Water problem

Water management often has a fragmented observation problem:

- point measurements describe local conditions;
- satellite observations describe territorial change but do not directly answer operational questions;
- environmental indicators are often analyzed separately;
- historical change is difficult to turn into a prioritized inspection queue;
- alerts can stop at a score without preserving why the signal matters, what is known, what is uncertain, and what should happen next.

The target problem for WTI is therefore:

> **Detect, localize and investigate water-relevant territorial change early enough to prioritize monitoring and intervention, while preserving the evidence chain behind every operational conclusion.**

This deliberately does **not** claim direct measurement of groundwater chemistry, discharge, flow or contamination from satellite embeddings alone.

The initial target is the broader and demonstrable class of **water-relevant territorial transformation**: contraction/expansion of water bodies, physical alteration around rivers, vegetation change associated with water systems, hydrologically relevant land-use transformation, and other environmental signals that justify deeper water investigation.

---

## 3. Proposed innovation

### Water Territorial Intelligence (WTI)

WTI is an adaptive intelligence layer for water systems that converts heterogeneous environmental observations into a traceable investigation cycle:

```text
WATER QUESTION
    ↓
TERRITORIAL REPRESENTATION
    ↓
TEMPORAL CHANGE / ANOMALY DETECTION
    ↓
MULTIMODAL CROSS-CHECK
    ↓
SPATIAL PRIORITIZATION
    ↓
EVIDENCE + PROVENANCE
    ↓
INVESTIGATION STATE
    ↓
NEXT RESEARCH / VALIDATION MOVE
    ↓
OBSERVATION
    ↓
STATE UPDATE
    ↺
```

The novelty to demonstrate is not "AI predicts water quality". That claim is not sufficiently supported by the current patrimony.

The defensible innovation is:

> **A water-intelligence workflow that turns satellite-derived territorial change into an auditable, adaptive investigation queue rather than a static map or alert.**

---

## 4. Architecture

```text
                         WATER TERRITORIAL INTELLIGENCE
┌─────────────────────────────────────────────────────────────────────┐
│ 1. QUESTION / TARGET                                                │
│    river | lake | reservoir | watershed | coastal water interface  │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 2. TERRITORIAL REPRESENTATION                                      │
│    AlphaEarth 64-D annual embeddings                               │
│    GhostWorks / TTI                                                │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 3. TEMPORAL CHANGE                                                 │
│    TTI / STT • annual deltas • trajectory • onset / drift         │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 4. MULTIMODAL WATER CONTEXT                                        │
│    Sentinel-1 SAR • Sentinel-2 NDVI • VIIRS / LST where available │
│    independent confirmation / contradiction                        │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 5. SPATIAL INTELLIGENCE                                             │
│    anomaly ranking • clusters • similar regions • retrieval       │
│    candidate queue / inspection priority                            │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 6. EVIDENCE / PROVENANCE                                           │
│    TraceFoundry: evidence → claim → gap → provenance               │
│    observed / inferred / hypothesis / insufficient / blocked       │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 7. ADAPTIVE INVESTIGATION                                          │
│    ASIE pattern: frontier → next move → observation → state update │
└───────────────────────────────┬─────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 8. OPERATIONAL OUTPUT                                              │
│    prioritized monitoring queue • evidence packet • next action   │
└─────────────────────────────────────────────────────────────────────┘
```

### Why this composition is coherent

The layers solve different problems and do not duplicate one another:

| Layer | Function | Existing asset | Status |
|---|---|---|---|
| Representation | Encode territorial state | AlphaEarth / GhostWorks | Existing |
| Change | Detect temporal transformation | TTI / STT | Existing, documented and deposited |
| Context | Cross-check physical/environmental change | Sentinel-1/2, SAR, NDVI, VIIRS | Existing in cases |
| Retrieval | Find and rank analogous territory | GhostWorks retrieval / similarity | Existing |
| Interpretation | Convert structured output to analyst-readable intelligence | GhostWorks serializer + agent prompt | Existing |
| Evidence | Preserve source-linked support | TraceFoundry | Existing |
| Provenance | Preserve source, timestamp, status and limitations | TraceFoundry | Existing |
| Investigation state | Track known/inferred/gaps | TraceFoundry | Existing |
| Adaptive next move | Choose what evidence to collect next | ASIE / Research Move pattern | Existing pattern; water integration required |
| Water semantics | Water-specific target ontology and rules | — | **Build** |
| Sensor integration | Real water-quality/level sensors | HydraLux concept | **Not demonstrated as operational evidence** |
| Operational dashboard | Water-specific interface | Legacy WaterLux material | **Build/compose** |

---

## 5. Concrete patrimony evidence

### 5.1 GhostWorks / AlphaEarth / TTI

**Evidence:** `viniburilux/ghostworks` and `viniburilux/TTI_Brazil_2017_2024`.

Concrete capabilities observed:

- 64-dimensional AlphaEarth satellite embeddings.
- TTI definition: `1 - cosine_similarity(E(x,t1), E(x,t2))`.
- Annual temporal trajectories.
- Relative annual deltas.
- Outlier/anomaly summaries.
- Spatial clustering.
- Similar-region retrieval in embedding space.
- Serializer producing structured JSON for an agent.
- Agent prompt explicitly designed to interpret trajectories, anomalies, clusters and similar regions.

### 5.2 Water-specific proof already present

The TTI repository contains a documented **Remanso/BA / São Francisco River** case:

- mean TTI: **0.133**;
- approximately **3.1× national mean**;
- maximum TTI: **0.690**;
- interpretation: extreme water-body retraction at Sobradinho Lake;
- importantly, the repository states this was captured **without a dedicated water mask**.

The same repository records independent validation:

- 36 candidate points;
- 47.2% with strong independent evidence;
- **80.5% with at least one independent sensor confirming transformation**.

These are the strongest existing quantitative anchors for a water-intelligence submission.

### 5.3 GhostWorks-ESG water signal

The GhostWorks-ESG paper records:

- Sentinel-1 SAR;
- Sentinel-2 NDVI;
- AlphaEarth semantic embeddings;
- VIIRS nighttime activity;
- 21 territorial hotspots around the Landulpho Alves Refinery in Bahia;
- a **+7.19 dB SAR anomaly near the Joanes River**, interpreted as significant physical alteration of a water body;
- evidence tied to coordinates and acquisition dates.

This proves that the territorial stack already reaches a water-adjacent physical signal and can combine multiple sensing modalities.

### 5.4 TraceFoundry

TraceFoundry already implements the evidence architecture needed around the environmental signal:

- `EvidenceReference`;
- `Claim` with epistemic statuses;
- `EvidenceGap`;
- versioned `InvestigationState`;
- `ResearchMove` with objective, action, rationale, evidence IDs, gap IDs, expected observation and stop criteria;
- provenance-bearing manifests;
- deterministic, explainable selection;
- explicit negative states such as insufficient, blocked and contradicted.

This is directly reusable for water observations once a geospatial/environmental adapter is added.

### 5.5 ASIE

The private/public archaeology documents an active `asie_experiment_v0` with three layers: exploration, reconstruction and comparison, and a broader pattern of adaptive investigation cycles.

The current public TraceFoundry contracts already expose the safe subset needed for a GPIW-facing artifact: state → gap → Research Move → expected observation → state update.

The internal frontier/scoring machinery should **not** be claimed as part of the public submission until the water-specific integration is reproduced and documented.

### 5.6 Legacy HydraLux / WaterLux

HydraLux/WaterLux contains useful architectural intent around hybrid sensing, predictive analytics and water governance. However, the archived material contains several claims that are not backed by the currently inspected technical repositories (for example, claimed sensor deployments, prediction accuracies, token transactions and protected-area metrics).

Therefore:

> **HydraLux/WaterLux is treated as a source of design intent, not as primary technical evidence.**

This distinction materially improves the credibility of the GPIW object.

### 5.7 LuxSense

The currently evidenced LuxSense implementation is a **Raman spectroscopy + ML industrial QC system**, with 3,510 spectra and 99.43% Random Forest accuracy on 702 test samples.

It demonstrates a general sensor-to-model pattern, but it is not a water sensor and therefore is **not part of the core WTI water evidence chain**. It may be cited only as evidence of broader sensing/ML capability if useful.

### 5.8 Capability horizon

The corpus also contains cross-domain territorial intelligence beyond the five water anchors: industrial and mining candidate retrieval, environmental/ecological investigations, temporal onset and early-mover reading, clustering, analogous-region search, structured serializer output and agent-oriented interpretation. These mechanisms are not being relabeled as water deployments. They are the transferable substrate from which WTI's larger architecture is composed.

---

## 6. What already works

### Demonstrated / documented

1. Semantic territorial representation from satellite embeddings.
2. Temporal change index calculation.
3. National-scale territorial aggregation.
4. Water-body transformation signal in the São Francisco/Sobradinho case.
5. Independent SAR/NDVI confirmation workflow.
6. Water-adjacent SAR anomaly in the Joanes River case.
7. Temporal trajectories and annual deltas.
8. Spatial anomaly and clustering outputs.
9. Similar-region retrieval.
10. Machine-readable territorial intelligence serialization.
11. Agent-oriented interpretation contract.
12. Evidence/provenance contracts.
13. Investigation state and explicit epistemic status.
14. Research Move contract with stop criteria.
15. Existing adaptive-investigation experiments outside the water domain.

---

## 7. What must be integrated

### Integration A — GhostWorks → Water Observation

Convert a GhostWorks observation into a canonical water observation:

```json
{
  "observation_id": "wti-...",
  "location": {"lat": 0, "lon": 0},
  "time_window": ["YYYY", "YYYY"],
  "signals": {
    "tti": null,
    "sar_delta": null,
    "ndvi_delta": null,
    "viirs_delta": null
  },
  "water_context": "river|lake|reservoir|coastal|unknown",
  "source": "...",
  "observed_at": "..."
}
```

### Integration B — Water Observation → TraceFoundry

Map the observation to:

`EvidenceReference → Claim → EvidenceGap → InvestigationState → ResearchMove`.

### Integration C — Adaptive loop

The first version does not need autonomous LLM planning. It needs a deterministic policy that demonstrates:

> strong water-relevant signal + weak corroboration → request corroboration;
> corroborated signal + known water context → prioritize inspection;
> contradictory signals → open contradiction/gap instead of issuing an alert.

### Integration D — Demonstration surface

A small water-specific report/dashboard should show:

- map/location;
- temporal trajectory;
- multimodal signal table;
- evidence status;
- uncertainty/gaps;
- next research move.

---

## 8. What needs to be built

### P0 — required for a convincing object

1. Water-specific observation schema.
2. GhostWorks-to-water adapter.
3. TraceFoundry-compatible investigation-state output.
4. Three real evidence cases:
   - Sobradinho/São Francisco water-body retraction;
   - Joanes River physical alteration signal;
   - São Paulo mangroves, Baía de Todos os Santos, and Aral Sea as aggregate frozen fixtures preserving documented evidence.
5. One offline demonstration that runs without GEE credentials using frozen derived values.
6. Evidence register with source, metric, time window and epistemic status.
7. Architecture diagram and reproducibility instructions.

### P1 — high-value extension

1. Water-context ontology.
2. Automatic water-relevance scoring.
3. Contradiction handling across SAR/NDVI/embedding signals.
4. Temporal onset detection.
5. Candidate prioritization benchmark: random/geographic baseline vs WTI queue.
6. Export to an operational dashboard.

### P2 — field/pilot layer

1. Real IoT water sensors.
2. Sensor calibration and QC.
3. Sensor-satellite fusion.
4. Field validation protocol.
5. Real-time alerting.
6. Pilot deployment with a water operator, basin committee, municipality, utility or research partner.

None of P2 should be represented as already operational unless new evidence is produced.

---

## 9. Demonstration we can produce now

### Demo: "From territorial change to a water investigation"

Input: frozen, already-documented GhostWorks/TTI results.

Output:

1. identify a water-relevant transformation signal;
2. show its temporal magnitude;
3. show independent sensor confirmation where available;
4. create an evidence packet;
5. classify each statement as observed / inferred / hypothesis / insufficient;
6. expose the missing evidence;
7. generate a Research Move;
8. produce a prioritized next action.

The key demo screen should therefore not be a generic dashboard. It should show:

```text
LOCATION
São Francisco / Sobradinho

SIGNAL
TTI mean 0.133
TTI max 0.690

WATER INTERPRETATION
Water-body retraction signal

CORROBORATION
Independent Sentinel-2 + SAR validation available

EVIDENCE STATUS
Observed: territorial transformation
Inferred: water-body retraction
Unknown: causal driver

NEXT MOVE
Inspect independent temporal imagery and water-specific contextual evidence

STOP CRITERION
Do not escalate to causal claim without independent corroboration
```

This is a much stronger GPIW demonstration than an invented "92% contamination prediction" because every displayed number can be traced to an existing artifact.

---

## 10. Maturity / TRL assessment

### Current demonstrable maturity

**System composition:** approximately **TRL 3–4** for the water-specific integrated object.

Reason:

- individual subsystems and research prototypes exist;
- water-specific evidence exists;
- the integrated water workflow is not yet demonstrated end-to-end in a field environment;
- no verified live water-sensor deployment is being claimed here;
- the adaptive investigation layer exists as a reusable architecture but still needs water-domain integration.

### What could move it toward TRL 4–5

- frozen end-to-end water case running reproducibly;
- three water cases instead of one;
- quantitative benchmark of prioritization;
- explicit TraceFoundry evidence chain;
- repeatable execution script and artifact bundle.

### What would support TRL 6–7

- operational pilot with real water observations;
- field validation against independent measurements;
- repeated operation over time;
- evidence that the queue improves monitoring/inspection efficiency or detection quality in a real deployment.

Do not claim TRL 6–7 solely from the legacy WaterLux narrative.

---

## 11. Relation to GPIW categories

The historical GPIW material already in the patrimony distinguishes:

- **Discovery Award:** TRL 1–3;
- **Breakthrough Award:** TRL 4–7;
- **Special Mentions / market-ready:** TRL 8–9.

The internal historical material also associates digitalization, automation and smart water management with the intended application space.

For the current object, the honest positioning is:

> **Discovery / early Breakthrough boundary today, with a credible path into Breakthrough after the integrated demonstration is completed.**

Because the current 2026 official form has not been re-verified in this inside-the-house pass, category wording should be checked against the live call before submission.

---

## 12. Submission gaps

| Gap | Severity | Can close internally? | Action |
|---|---|---:|---|
| Water-specific integrated demo | Closed for frozen fixtures; live integration remains | Yes | Maintain offline adapter and integrate live source outputs |
| Raw/point-level evidence bundle | Medium | Partly | Recover raw artifacts for aggregate fixtures where redistribution is permitted |
| Water ontology | Medium | Yes | Define river/lake/reservoir/coastal contexts |
| Evidence/provenance bridge | Critical | Yes | Emit TraceFoundry-compatible state |
| Adaptive next-move loop | High | Yes | Implement deterministic first policy |
| Live sensor data | High | No, not from current evidence | Partner/pilot required |
| Field validation | High | No | External field measurement required |
| Quantitative operational benchmark | High | Yes initially | Compare WTI prioritization against baselines |
| Current GPIW 2026 form/category wording | Medium | No, requires official call check | Verify before final submission |
| Legacy WaterLux claims | Critical if reused | Yes | Remove or relabel as unverified design claims |

---

## 13. Recommended object for submission

### Working title

**Water Territorial Intelligence: Adaptive Detection and Investigation of Water-Relevant Environmental Change**

### One-sentence innovation

> A low-cost water-intelligence architecture that combines satellite semantic embeddings, temporal change detection, multimodal environmental evidence and adaptive investigation to turn territorial signals into traceable monitoring priorities and next actions.

### What makes it ours

The individual data sources are public. The proprietary/intellectual contribution is the **composition and operational contract**:

`territorial representation → change → corroboration → evidence → investigation state → next move`.

The system is therefore not being presented as a new satellite sensor or new foundation model. It is a **decision/investigation architecture built around capabilities we have already implemented and demonstrated in adjacent domains and water-relevant cases**.

---

## 14. Build order

1. Freeze evidence.
2. Build water observation schema.
3. Build GhostWorks → WTI adapter.
4. Emit TraceFoundry investigation state.
5. Add Research Move policy.
6. Reproduce Sobradinho case offline.
7. Add Joanes case.
8. Add third water case if evidence can be recovered.
9. Run prioritization benchmark.
10. Package demo + architecture + evidence register.
11. Only then write the final GPIW application narrative.

---

## 15. Non-claims

This architecture does **not** currently establish:

- real-time water-quality measurement;
- groundwater chemistry inference;
- contamination prediction accuracy;
- field sensor deployment;
- causal attribution of detected territorial changes;
- autonomous water-management decisions;
- TRL 6–7 field maturity.

Those are future validation targets, not current evidence.

---

## 16. Bottom line

The patrimony already contains the seed of a real Water Intelligence technology.

The strongest path is to **reframe GhostWorks as the observation/representation engine, use TTI as the water-relevant change detector, use independent satellite signals as corroboration, and use TraceFoundry/ASIE as the evidence-aware adaptive investigation layer.**

HydraLux/WaterLux then becomes the historical water-domain design lineage rather than the technical proof base.

That composition produces a coherent object that can be demonstrated now and extended toward field water intelligence later.
