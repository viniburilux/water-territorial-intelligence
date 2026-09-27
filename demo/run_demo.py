from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from water_intelligence_adapter import run

root = Path(__file__).resolve().parent
cases = ["sobradinho", "joanes", "sao-paulo-mangroves", "baia-todos-os-santos", "aral-sea"]
for case in cases:
    observation = root / case / "observation.json"
    out = root / "outputs" / case
    run(str(observation), str(out))
    obs = json.loads(observation.read_text(encoding="utf-8"))
    corroboration = obs.get("corroboration", {})
    agreement = corroboration.get("agreement_rate")
    agreement_text = f"{agreement:.1%}" if isinstance(agreement, (int, float)) else "documented / not quantified in fixture"
    print(f"WTI investigation state — {case}")
    print(f"  context: {obs['water_context']}")
    print(f"  signal: {obs['interpretation']}")
    print(f"  corroboration: {agreement_text}")
    print("  evidence state: observed signal; causal driver insufficient")
    print("  next research move: corroborate territorial change")
    print(f"  outputs: {out}")
