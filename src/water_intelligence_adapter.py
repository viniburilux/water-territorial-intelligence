"""Offline WTI adapter: frozen observation -> traceable investigation state."""
from __future__ import annotations
import json
from pathlib import Path


def build_state(obs: dict, generated_at: str | None = None) -> tuple[dict, dict]:
    oid = obs["observation_id"]
    inv = f"investigation-{oid}"
    ev = f"ev-{oid}"
    claim_signal = f"claim-signal-{oid}"
    claim_causal = f"claim-causal-{oid}"
    gap_causal = f"gap-causal-{oid}"
    move = f"move-corroborate-{oid}"
    source_observed_at = obs.get("source_observed_at")
    factual_time = source_observed_at

    evidence = [{
        "evidence_id": ev,
        "kind": "environmental_observation",
        "source": obs["source"],
        "uri": obs.get("evidence_uri"),
        "record_id": oid,
        "source_observed_at": source_observed_at,
        "metadata_only": True,
        "provenance_note": "Frozen derived observation from an existing project artifact; no live acquisition performed by this demo.",
        "source_artifact": obs.get("source_artifact"),
        "signals": obs.get("signals", {}),
        "corroboration": obs.get("corroboration"),
        "limitations": obs.get("limitations", []),
    }]
    state = {
        "schema_version": "tracefoundry.investigation_state.v0",
        "investigation_id": inv,
        "question": f"What water-relevant territorial change is evidenced at {obs['location'].get('label', oid)}, and what should be investigated next?",
        "status": "in_review",
        "evidence": evidence,
        "claims": [
            {"claim_id": claim_signal, "statement": "The existing artifact contains a documented environmental transformation signal at the stated location and period.", "status": "observed", "evidence_ids": [ev], "gap_ids": []},
            {"claim_id": claim_causal, "statement": "The available artifact establishes the causal driver of the water-relevant change.", "status": "insufficient", "evidence_ids": [ev], "gap_ids": [gap_causal], "note": "Causal attribution is intentionally not inferred from the frozen metrics."}
        ],
        "gaps": [{"gap_id": gap_causal, "statement": "Independent water-specific context is insufficient to attribute the observed transformation to a specific driver.", "severity": "high", "required_evidence": ["independent temporal imagery", "water-specific contextual data", "field or authoritative hydrological evidence where available"], "status": "open"}],
        "decision": "Prioritize corroboration and contextual investigation; do not escalate to causal attribution.",
        "next_move_id": move,
        "source_observed_at": factual_time,
        "generated_at": generated_at,
        "warnings": ["Offline fixture only", "No live sensor measurement", "No causal inference"]
    }
    research_move = {
        "schema_version": "tracefoundry.research_move.v0",
        "move_id": move,
        "investigation_id": inv,
        "title": "Corroborate water-relevant territorial change",
        "objective": "Reduce the causal/interpretive gap before issuing an operational water-risk conclusion.",
        "action_type": "validate",
        "action": "Compare the existing territorial signal against independent temporal imagery and water-specific contextual evidence for the same location and period.",
        "rationale": "The signal is already observable in the existing artifact, but the current evidence does not establish its driver.",
        "evidence_ids": [ev], "gap_ids": [gap_causal],
        "expected_observation": "Either independent evidence corroborates the water-relevant interpretation, or the investigation records contradiction/insufficient evidence.",
        "stop_criteria": ["Do not attribute causality without independent corroboration.", "If sources contradict one another, preserve the contradiction instead of averaging it away.", "If evidence remains insufficient, keep the claim at observed/inferred status."],
        "status": "proposed", "source_observed_at": factual_time, "generated_at": generated_at,
        "provenance_note": "Generated offline from the WTI demonstration contract."
    }
    return state, research_move


def run(path: str, out_dir: str, generated_at: str | None = None) -> None:
    obs = json.loads(Path(path).read_text(encoding="utf-8"))
    state, move = build_state(obs, generated_at=generated_at)
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    (out / "investigation_state.json").write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "research_move.json").write_text(json.dumps(move, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("observation")
    p.add_argument("--out", default="demo/output")
    p.add_argument("--generated-at", default=None, help="Optional execution timestamp; omitted for deterministic output")
    args = p.parse_args()
    run(args.observation, args.out, generated_at=args.generated_at)
