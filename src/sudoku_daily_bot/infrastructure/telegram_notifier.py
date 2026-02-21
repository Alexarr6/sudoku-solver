import requests


class TelegramNotifier:
    def __init__(self, bot_token: str, chat_id: str, timeout_seconds: int = 15) -> None:
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.timeout_seconds = timeout_seconds

    def send(self, message: str) -> None:
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        response = requests.post(
            url,
            json={"chat_id": self.chat_id, "text": message},
            timeout=self.timeout_seconds,
        )
        response.raise_for_status()
