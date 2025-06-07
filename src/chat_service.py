class ChatService:
    """Client for interacting with the Pollinations Chat Completions API."""

    def __init__(self, endpoint: str = "https://text.pollinations.ai/openai", model: str = "openai-large", timeout: int = 5):
        self.endpoint = endpoint
        self.model = model
        self.timeout = timeout

    def ask(self, persona: str, question: str) -> str:
        """Send the persona and question to the API and return the response."""
        import requests

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": persona},
                {"role": "user", "content": question},
            ],
        }
        try:
            resp = requests.post(self.endpoint, json=payload, timeout=self.timeout)
            if resp.ok:
                data = resp.json()
                return (
                    data.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content", "...")
                    .strip()
                )
        except Exception:
            pass
        return "..."
