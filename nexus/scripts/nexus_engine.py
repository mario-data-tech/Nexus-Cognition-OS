import os
import sys
import json
import argparse
from pathlib import Path

NEXUS_DIR = ".nexus"
LEDGER_FILE = "ledger.json"

def get_nexus_path(root: Path) -> Path:
    return root / NEXUS_DIR

def init_nexus(root: Path, goal: str):
    nexus_path = get_nexus_path(root)
    nexus_path.mkdir(exist_ok=True)
    
    state = {
        "goal": goal,
        "next_action": "Initial state set. Begin execution.",
        "core_hub": {},
        "checkpoints": [],
        "questions": []
    }
    
    ledger_path = nexus_path / LEDGER_FILE
    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    print(f"Nexus initialized successfully at {nexus_path}")

def load_state(root: Path) -> dict:
    ledger_path = get_nexus_path(root) / LEDGER_FILE
    if not ledger_path.exists():
        raise FileNotFoundError("Nexus not initialized. Run 'init' first.")
    with open(ledger_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(root: Path, state: dict):
    ledger_path = get_nexus_path(root) / LEDGER_FILE
    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def cmd_goal(root: Path, action: str):
    state = load_state(root)
    state["next_action"] = action
    save_state(root, state)
    print(f"Next action updated: {action}")

def cmd_status(root: Path):
    state = load_state(root)
    print(json.dumps(state, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Nexus-Cognition OS Controller")
    parser.add_argument("--root", default=".", help="Workspace root directory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    parser_init = subparsers.add_parser("init", help="Initialize Nexus workspace")
    parser_init.add_argument("goal", help="Main goal of the task")

    # goal / next action update
    parser_goal = subparsers.add_parser("goal", help="Update next action")
    parser_goal.add_argument("action", help="Next action description")

    # status
    subparsers.add_parser("status", help="Show current ledger status")

    args = parser.parse_args()
    root = Path(args.root)

    if args.command == "init":
        init_nexus(root, args.goal)
    elif args.command == "goal":
        cmd_goal(root, args.action)
    elif args.command == "status":
        cmd_status(root)

if __name__ == "__main__":
    main()
