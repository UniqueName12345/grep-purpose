# grep-purpose

> ...where `ps aux` just lists your regrets.

`grep-purpose` is a FOSS, terminal-only life simulator written in C++. Think *The Sims*, but stripped of all pretense, prettiness, and joy—just you, a shell, and a facsimile of existence that barely holds together. And yes, it will be MIT-licensed, because freedom includes the right to simulate a deeply mediocre life.

## 🧠 What *is* this?

This is a bizarre attempt to model a human-like life—sleeping, eating, working, spiraling—in a terminal window. It won’t have any fancy graphics. It might barely have ASCII. What it *will* have is a complex, extensible simulation of:

- Human needs (hunger, hygiene, social, etc.)
- Time, schedules, and existential dread
- Jobs, relationships, purchases, and death
- Procedural NPCs with actual personalities
- And probably a way to name your fridge “Greg” and talk to it

## 🎯 Project Goals

At this early brainstorming stage, the goals are:

- [ ] Define core simulation systems (needs, time, relationships)
- [ ] Outline a data structure for representing the world and its agents
- [ ] Build an interface that works entirely in the terminal (no GUI)
- [ ] Allow scripting or modding (Lua? Python? or just config files?)
- [ ] Embrace chaos: allow for glitches, absurdity, and unintended life paths
- [ ] Run on Linux, Windows (via terminal), macOS, and hopefully a toaster

## 🛠️ Tech Stack (Planned)

- **Language:** C++
- **UI:** Terminal / TUI (likely ncurses or equivalent later on)
- **License:** MIT
- **Build System:** Probably CMake, eventually

## 🔧 Building

To build on Windows you'll need [CMake](https://cmake.org/) and a make tool.
Install either the Visual Studio Build Tools (providing `nmake`) or MinGW
(`mingw32-make`). Running `build.bat` will pick the appropriate generator if one
of those tools is on your `PATH`.

To force a different generator, set the `generator` environment variable before
invoking the script:

```cmd
set generator=Unix Makefiles
build.bat
```

## 🪦 Why?

Why not? Life's already hard enough—why not simulate it in 80x24 characters?

## 🔓 License

MIT License. See [`LICENSE`](LICENSE) for full details.

You are free to fork, modify, and expand the project. You’re also free to regret doing so, as is tradition.

---

> **Note:** This project is in the **pre-prototype** stage. A small skeleton exists with an NPC class and simple build system. Contributions to the design discussion are still welcome, even if they're just "make the toilet break randomly."

