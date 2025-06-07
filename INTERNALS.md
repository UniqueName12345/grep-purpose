# Internal Design

This document outlines the main modules that make up **grep-purpose** and how they interact. It is intended for contributors who want a quick tour of the codebase.

## Directory layout

- `src/`
  - `main.py` – command line entry point. Sets up the simulation loop and handles user input.
  - `simulation.py` – manages global time and updates all NPCs each tick.
  - `npc.py` – defines the `NPC` class with basic needs, relationships and actions.
  - `chat_service.py` – small client for the Pollinations text APIs used for NPC dialogue.
  - `io_utils.py` – thin wrappers around `print` and `input` for possible future expansion.

### NPC dialogue

NPC conversations rely on the free Pollinations API. By default `ChatService` posts to the OpenAI-compatible endpoint. You can switch to the simpler GET API:

```python
from chat_service import ChatService
service = ChatService(use_get=True)
```

This packs the persona and question into a single URL request like `https://text.pollinations.ai/{persona} Q: {question} A:`.
