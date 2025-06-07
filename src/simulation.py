class Simulation:
    """Simple world state handling time progression and NPC updates."""

    def __init__(self):
        self.hour = 0
        self.day = 0
        self.npcs = []

    def add_npc(self, npc):
        self.npcs.append(npc)

    def tick(self):
        """Advance time by one hour and update NPCs."""
        self.hour += 1
        if self.hour >= 24:
            self.hour = 0
            self.day += 1
        from io_utils import fprint
        import random

        for npc in list(self.npcs):
            npc.tick()
            if npc.alive and random.random() < 0.05:
                npc.die()
                fprint(f"{npc.name} died in a tragic collision!")
                self.npcs = [n for n in self.npcs if n.alive]

    def time_str(self) -> str:
        return f"Day {self.day} Hour {self.hour:02d}"
