# Evidence Register — WTI

This register keeps empirical evidence, executable fixtures and epistemic status distinct. A fixture is executable when the frozen observation can be loaded by the offline adapter; this does not imply that all raw historical inputs are redistributed here.

| ID | Case | Source artifact | Evidence | Status | Fixture |
|---|---|---|---|---|---|
| E-SOB-01 | Sobradinho / São Francisco | TTI_Brazil_2017_2024 `TTI_Summary.md` | STT mean 0.1326; median 0.0679; P90 0.3697; P99 0.6358; max 0.6898 | observed | `demo/sobradinho/observation.json` |
| E-SOB-02 | Sobradinho / São Francisco | same | 29/36 candidates had at least one Sentinel-1/Sentinel-2 agreement (80.5%) | observed | same |
| E-SOB-03 | Sobradinho / São Francisco | same | Water-body retraction interpretation | inferred | same |
| E-JOA-01 | Rio Joanes | GhostWorks `consolidated_data.md` (Case 01); internal GhostWorks-ESG case record | P03 coordinate -12.8176, -38.3315; SAR +7.19 dB; NDVI -0.741 | observed | `demo/joanes/observation.json` |
| E-JOA-02 | Rio Joanes | same | Historical imagery corroboration available | observed | same |
| E-JOA-03 | Rio Joanes | same | Physical alteration interpretation | inferred | same |
| E-MAN-01 | São Paulo mangroves | GhostWorks AuditLab + territorial dossier | ~4,000 points; 2018–2024; 20 alerts; Dynamic World/MapBiomas/GMW/VIIRS/Sentinel-2 | observed | `demo/sao-paulo-mangroves/observation.json` |
| E-BTS-01 | Baía de Todos os Santos | GhostWorks_BTS_v1 / Leitura_Territorial_BTS | 33,600 embeddings; 64 dimensions; 8 territories; STT comparison | observed | `demo/baia-todos-os-santos/observation.json` |
| E-ARAL-01 | Aral Sea | GhostWorks Atlas | State/transition trajectory; outliers; clusters; analogous regions; 2018–2024 | observed | `demo/aral-sea/observation.json` |
| E-TF-01 | Provenance layer | TraceFoundry contracts | EvidenceReference, Claim, EvidenceGap, InvestigationState and Research Move pattern | observed (design reused) | `src/`, `schemas/` |

## Documentary origin notes

- **Rio Joanes:** the public GhostWorks repository documents hotspot P03, its coordinate and the qualitative water-body alteration finding (`consolidated_data.md`, Case 01). The numeric SAR (+7.19 dB), NDVI (-0.741) and hotspot score values are recorded in the internal GhostWorks-ESG case record, which has not yet been redistributed in a public artifact. The values are kept with their documentary origin rather than removed (traceability, not suppression); publishing a redistributable extract is on the [roadmap](roadmap.md).

## Important exclusions

WTI does not claim live IoT sensing, groundwater chemistry, causal attribution, field validation, deployed users, commercial traction or hydrological forecasting. GMW = 0 ha at a point is not treated as proof of mangrove absence, and STT is not automatically hydrological degradation.
