from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "demo"
SLUGS = ["sobradinho", "joanes", "sao-paulo-mangroves", "baia-todos-os-santos", "aral-sea"]


class WTIIntegrationTests(unittest.TestCase):
    def test_all_observations_match_schema(self):
        schema = json.loads((ROOT / "schemas/water_observation.schema.json").read_text())
        validator = Draft202012Validator(schema)
        for slug in SLUGS:
            data = json.loads((FIXTURE_DIR / slug / "observation.json").read_text())
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            self.assertEqual(errors, [], f"{slug}: {errors}")

    def test_demo_generates_both_outputs_for_all_cases(self):
        out = ROOT / "demo/outputs"
        if out.exists():
            shutil.rmtree(out)
        result = subprocess.run([sys.executable, "demo/run_demo.py"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        for slug in SLUGS:
            self.assertTrue((out / slug / "investigation_state.json").exists())
            self.assertTrue((out / slug / "research_move.json").exists())

    def test_outputs_match_their_schemas(self):
        state_schema = json.loads((ROOT / "schemas/investigation_state.schema.json").read_text())
        move_schema = json.loads((ROOT / "schemas/research_move.schema.json").read_text())
        for slug in SLUGS:
            state = json.loads((ROOT / "demo/outputs" / slug / "investigation_state.json").read_text())
            move = json.loads((ROOT / "demo/outputs" / slug / "research_move.json").read_text())
            Draft202012Validator(state_schema).validate(state)
            Draft202012Validator(move_schema).validate(move)

    def test_same_input_produces_same_factual_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a", Path(tmp) / "b"
            fixture = FIXTURE_DIR / "sao-paulo-mangroves/observation.json"
            subprocess.run([sys.executable, "src/water_intelligence_adapter.py", str(fixture), "--out", str(a)], cwd=ROOT, check=True)
            subprocess.run([sys.executable, "src/water_intelligence_adapter.py", str(fixture), "--out", str(b)], cwd=ROOT, check=True)
            for name in ("investigation_state.json", "research_move.json"):
                ha = hashlib.sha256((a / name).read_bytes()).hexdigest()
                hb = hashlib.sha256((b / name).read_bytes()).hexdigest()
                self.assertEqual(ha, hb, name)


if __name__ == "__main__":
    unittest.main()
