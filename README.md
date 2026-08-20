# Nexus-Cognition OS v1.0.0

A model-agnostic inference-time cognitive control system for deep reasoning, long-horizon work, tool use, verification, and recovery.

## Quick Start
Initialize the workspace and track tasks using the CLI controller:
```bash
python -m nexus.scripts.nexus_engine --root . init "Build Nexus-Cognition OS"
python -m nexus.scripts.nexus_engine --root . goal "Complete core modules"
python -m nexus.scripts.nexus_engine --root . status
