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
        # Alive state for permadeath
        self.alive = True

    def tick(self) -> None:
        """Simulate the passage of time for this NPC."""
        if not self.alive:
            return
        self.hunger = min(100, self.hunger + 10)
        self.energy = max(0, self.energy - 5)
        self.social = max(0, self.social - 2)

    def eat(self) -> None:
        """Restore some hunger."""
        self.hunger = max(0, self.hunger - 40)

    def sleep(self) -> None:
        """Restore energy."""
        self.energy = min(100, self.energy + 40)

    def die(self) -> None:
        """Mark NPC as dead permanently."""
        self.alive = False

    def talk_to(self, other: "NPC") -> None:
        """Improve relationship with another NPC and get a generated reply."""
        from io_utils import fprint
        import requests

        if not self.alive or not other.alive:
            return

        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        self.relationships[other.name] += 5
        self.social = min(100, self.social + 10)

        fprint(f"{other.name} is thinking...")
        prompt = f"Say something to {self.name}."
        try:
            resp = requests.post(
                "https://text.pollinations.ai/openai",
                json={"model": "openai-large", "prompt": prompt},
                timeout=5,
            )
            if resp.ok:
                data = resp.json()
                message = data.get("choices", [{}])[0].get("text", "...").strip()
            else:
                message = "..."
        except Exception:
            message = "..."
        fprint(f"{other.name}: {message}")

    def describe(self) -> str:
        """Return a short description of the NPC's current state."""
        if not self.alive:
            return f"{self.name} is dead."
        return (
            f"{self.name} ({self.age}) - "
            f"hunger:{self.hunger}% energy:{self.energy}% social:{self.social}%"
        )
