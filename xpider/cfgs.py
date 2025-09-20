import json
from typing import Optional
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/58.0.3029.110 Safari/537.36"
)

CONFIG = {
    "headers": {
        "User-Agent": DEFAULT_USER_AGENT,
        "Cookie": "",
        "Referer": "",
        "Content-Type": "",
    },
    "interval": (0, 12),  # 爬取间隔, 单位秒, 0~1s之间, 元组形式
}


class GetConfig:
    """
    CONFIG = {
    "headers": {
        "User-Agent": DEFAULT_USER_AGENT,
        "Cookie": "",
        "Referer": "",
        "Content-Type": "",
    },
    "interval": (0, 1),  # 爬取间隔, 单位秒, 0~1s之间, 元组形式
    }
    """

    def __init__(self, k: Optional[str] = None):
        self.k = k

    def __call__(self):
        return CONFIG[self.k] if self.k else CONFIG

    def get(self, k):
        return CONFIG[k]

    def set(self, k, v: str):
        CONFIG[k] = v


def save_config():
    with open("xpider.json", "w", encoding="utf-8") as f:
        json.dump(GetConfig()(), f, ensure_ascii=False, indent=4)
