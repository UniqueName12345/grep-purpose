# INTERNALS.md

Welcome to the absolute mess that is **grep-purpose**'s internal design. This file exists so new contributors don’t have to grep the whole codebase just to figure out why their NPC is eating carpet instead of food.

---

## 🗂️ Directory Layout (A.K.A. “How We Organize Our Chaos”)

- `src/`
  - `main.py` – The command line bouncer. Sets up the simulation, runs the endless loop, and pretends to handle your input gracefully.
  - `simulation.py` – The beating, caffeine-fueled heart. Advances time and makes all NPCs do their regrettable little routines each tick.
  - `npc.py` – Home of the `NPC` class. Needs, relationships, actions—basically where your fake friends are born and slowly lose the will to live.
  - `chat_service.py` – A glorified text generator. Talks to Pollinations text APIs so your NPCs can say things like “I am afraid” or “Why am I here?”
  - `io_utils.py` – Wrappers around `print` and `input`. Someday we might need this abstraction. Today, it’s just here to look pretty.

---

## 💬 NPC Dialogue (Or, “Why Is My Sim Quoting Schopenhauer?”)

NPCs try to be relatable by talking to the [Pollinations API](https://text.pollinations.ai/). The simpler GET API is now the default because the OpenAI-compatible endpoint is a bit broken. If you want to try the OpenAI flavor anyway, pass `use_get=False` or toggle it in the TUI settings:

```python
from chat_service import ChatService
service = ChatService()  # uses the GET API by default
```

Need to feel brave? Use the OpenAI endpoint instead:

```python
service = ChatService(use_get=False)
```

This will squish both the persona and the burning question into a single GET request, like:

```
https://text.pollinations.ai/{persona} Q: {question} A: 
```

It’s beautiful. It’s horrifying. Sometimes, it even works.

---

## 🚨 Important Design Notes

* This is a C++ project in spirit, but the layout above is a fever dream of what a Python version *would* look like. Adjust accordingly, and try not to cry.
* Anything not documented here is either “self-explanatory” or a complete mystery even to us.
* If your NPC does something weird, blame `simulation.py`. That’s what we do.

---

Feel free to add your own modules, just don’t name them after real emotions.
