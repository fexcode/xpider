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
    "interval": 10,
}


def get_cfg(k: Optional[str] = None):
    # 配置随时都有可能被更新, 直接导入可能是以常量保存的, 所以写这个函数来获取配置
    return CONFIG[k] if k else CONFIG


def save_config():
    with open("xpider.json", "w", encoding="utf-8") as f:
        json.dump(get_cfg(), f, ensure_ascii=False, indent=4)
