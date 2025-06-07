class NPC:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Basic needs
        self.hunger = 0
        self.energy = 100
        self.social = 50
        # Relationships with other NPCs by name
        self.relationships = {}

    def tick(self) -> None:
        """Simulate the passage of time for this NPC."""
        self.hunger = min(100, self.hunger + 10)
        self.energy = max(0, self.energy - 5)
        self.social = max(0, self.social - 2)

    def eat(self) -> None:
        """Restore some hunger."""
        self.hunger = max(0, self.hunger - 40)

    def sleep(self) -> None:
        """Restore energy."""
        self.energy = min(100, self.energy + 40)

    def talk_to(self, other: "NPC") -> None:
        """Improve relationship with another NPC."""
        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        self.relationships[other.name] += 5
        self.social = min(100, self.social + 10)

    def describe(self) -> str:
        """Return a short description of the NPC's current state."""
        return (
            f"{self.name} ({self.age}) - "
            f"hunger:{self.hunger}% energy:{self.energy}% social:{self.social}%"
        )
