class Simulation:
    """Simple world state handling time progression and NPC updates."""

    def __init__(self, collision_probability: float = 0.05):
        self.hour = 0
        self.day = 0
        self.npcs = []
        self.collision_probability = collision_probability

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

        death_messages = []

        alive_npcs = [n for n in self.npcs if n.alive]
        if len(alive_npcs) >= 2 and random.random() < self.collision_probability:
            a, b = random.sample(alive_npcs, 2)
            a.die()
            b.die()
            death_messages.append(
                f"{a.name} collided with {b.name} and they both died!"
            )

        for npc in self.npcs:
            before_alive = npc.alive
            npc.tick()
            if before_alive and not npc.alive:
                death_messages.append(f"{npc.name} starved to death!")

        self.npcs = [n for n in self.npcs if n.alive]

        for msg in death_messages:
            fprint(msg)

    def time_str(self) -> str:
        return f"Day {self.day} Hour {self.hour:02d}"
