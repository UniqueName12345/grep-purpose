PLACES = {
    "White Void": {"cost": 0, "hunger": 0, "energy": 0, "social": 0},
    "Park": {"cost": 0, "hunger": 0, "energy": -20, "social": 30},
    "Fast Food": {"cost": 5, "hunger": -40, "energy": 0, "social": 0},
    "Mall": {"cost": 10, "hunger": 0, "energy": -10, "social": 25},
}


class NPC:
    def __init__(self, name: str, age: int, persona: str = ""):
        self.name = name
        self.age = age
        self.persona = persona
        # Basic needs
        self.hunger = 0
        self.energy = 100
        self.social = 50
        # Money
        self.money = 1000
        # Current location
        self.location = "White Void"
        # Relationships with other NPCs by name
        self.relationships = {}
        # Alive state for permadeath
        self.alive = True

    def tick(self) -> None:
        """Simulate the passage of time for this NPC."""
        if not self.alive:
            return
        self.hunger = min(100, self.hunger + 10)
        self.energy = max(0, self.energy - 5)
        self.social = max(0, self.social - 2)

        self.location = self.choose_place()
        self.apply_place_effects()
        if self.hunger >= 100:
            self.die()

    def eat(self) -> None:
        """Restore some hunger."""
        self.hunger = max(0, self.hunger - 40)

    def sleep(self) -> None:
        """Restore energy."""
        self.energy = min(100, self.energy + 40)

    def choose_place(self) -> str:
        """Decide where to go this tick based on needs and money."""
        import random

        if self.hunger > 70 and self.money >= PLACES["Fast Food"]["cost"]:
            return "Fast Food"
        if self.social < 30:
            if self.money >= PLACES["Mall"]["cost"] and random.random() < 0.5:
                return "Mall"
            return "Park"
        return "White Void"

    def apply_place_effects(self) -> None:
        """Apply effects of the current location."""
        effects = PLACES.get(self.location, {})
        self.hunger = max(0, min(100, self.hunger + effects.get("hunger", 0)))
        self.energy = max(0, min(100, self.energy + effects.get("energy", 0)))
        self.social = max(0, min(100, self.social + effects.get("social", 0)))
        cost = effects.get("cost", 0)
        if self.money >= cost:
            self.money -= cost

    def die(self) -> None:
        """Mark NPC as dead permanently."""
        self.alive = False

    def talk_to(self, other: "NPC", question: str, chat_service=None) -> None:
        """Ask another NPC a question and show their persona-based answer."""
        from io_utils import fprint
        from chat_service import ChatService

        if not self.alive or not other.alive:
            return

        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        self.relationships[other.name] += 5
        self.social = min(100, self.social + 10)

        fprint(f"{other.name} is thinking...")

        if chat_service is None:
            chat_service = ChatService()

        message = chat_service.ask(other.persona, question)
        fprint(f"{other.name}: {message}")

    def describe(self) -> str:
        """Return a short description of the NPC's current state."""
        if not self.alive:
            return f"{self.name} is dead."
        return (
            f"{self.name} ({self.age}) @ {self.location} - "
            f"hunger:{self.hunger}% energy:{self.energy}% social:{self.social}% "
            f"$ {self.money}"
        )
