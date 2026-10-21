import requests
from config import Config


class AIServiceError(Exception):
    pass


class AIService:

    def sistem_talimati(self):
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):

        if not Config.GROQ_API_KEY:
            return "Demo modu: API anahtari bulunamadi."

        if gecmis is None:
            gecmis = []

        messages = [
            {
                "role": "system",
                "content": self.sistem_talimati()
            }
        ]

        messages.extend(gecmis)

        messages.append({
            "role": "user",
            "content": mesaj
        })

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {Config.GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-oss-20b",
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

        except requests.RequestException as hata:
            raise AIServiceError(
                "Yapay zeka servisine baglanirken hata olustu."
            ) from hata


ai_service = AIService()
