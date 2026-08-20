import unittest
from pathlib import Path
import shutil
import json

from nexus.scripts import nexus_engine

class TestNexusEngine(unittest.TestCase):
    def setUp(self):
        self.test_root = Path("test_workspace")
        self.test_root.mkdir(exist_ok=True)

    def tearDown(self):
        if self.test_root.exists():
            shutil.rmtree(self.test_root)

    def test_init_and_status(self):
        nexus_engine.init_nexus(self.test_root, "Test Goal")
        state = nexus_engine.load_state(self.test_root)
        self.assertEqual(state["goal"], "Test Goal")
        self.assertIn("next_action", state)

    def test_update_goal(self):
        nexus_engine.init_nexus(self.test_root, "Initial Goal")
        nexus_engine.cmd_goal(self.test_root, "New action step")
        state = nexus_engine.load_state(self.test_root)
        self.assertEqual(state["next_action"], "New action step")

if __name__ == "__main__":
    unittest.main()
