class NPC:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hunger = 0
        self.energy = 100

    def tick(self) -> None:
        """Simulate the passage of time for this NPC."""
        self.hunger = min(100, self.hunger + 10)
        self.energy = max(0, self.energy - 5)

    def describe(self) -> str:
        """Return a short description of the NPC's current state."""
        return f"{self.name} ({self.age}) - hunger:{self.hunger}% energy:{self.energy}%"
