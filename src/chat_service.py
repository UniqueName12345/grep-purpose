class ChatService:
    """Client for interacting with the Pollinations text APIs."""

    def __init__(
        self,
        endpoint: str = "https://text.pollinations.ai/openai",
        model: str = "openai-large",
        timeout: int = 5,
        use_get: bool = True,
    ):
        self.endpoint = endpoint
        self.model = model
        self.timeout = timeout
        self.use_get = use_get

    def ask(self, persona: str, question: str) -> str:
        """Send the persona and question to the API and return the response."""
        import requests
        import urllib.parse

        if self.use_get:
            prompt = f"{persona} Q: {question} A:"
            url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}"
            try:
                resp = requests.get(url, timeout=self.timeout)
                if resp.ok:
                    return resp.text.strip()
            except Exception:
                pass
            return "..."

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
