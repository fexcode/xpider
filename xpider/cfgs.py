import json
from typing import Optional

CONFIG = {
    "headers": {
        "user_agent": "",
        "cookie": "",
        "referer": "",
        "origin": "",
        "accept": "*/*",
        "accept_encoding": "gzip, deflate, br",
        "accept_language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content_type": "",
    },
    "interval": 10,
}


def get_cfg(k: Optional[str] = None):
    # 配置随时都有可能被更新, 直接导入可能是以常量保存的, 所以写这个函数来获取配置
    return CONFIG[k] if k else CONFIG


def save_config():
    with open("xpider.json", "w", encoding="utf-8") as f:
        json.dump(get_cfg(), f, ensure_ascii=False, indent=4)
