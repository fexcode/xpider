import requests
import sys
from typing import Callable, Optional, Any
from ..interfaces import XTask
from ..cfgs import get_cfg


if sys.version_info < (3, 10):
    CALLABLE = Callable[[requests.Response], Any]
else:
    from typing import TypeAlias

    CALLABLE: TypeAlias = Callable[[requests.Response], Any]


class Request(XTask):
    """
    内部类, 用于处理 requests 请求
    """

    def __init__(self, method: str, url: str, callback: CALLABLE, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.callback = callback

    def run(self) -> requests.Response:

        response = requests.request(
            method=self.method,
            url=self.url,
            headers=(get_cfg("headers")),
            **self.kwargs,
        )
        self.callback(response)
        return response


class GetRq(Request):
    """
    Get请求一个网址

    参数:
        url: 网址
        callback: 回调函数, 接收 requests.Response 对象作为参数
    """

    def __init__(self, url: str, callback: CALLABLE, **kwargs):
        super().__init__("GET", url, callback, **kwargs)


class PostRq(Request):
    """
    Post请求一个网址
    """

    def __init__(
        self,
        url: str,
        callback: CALLABLE,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        **kwargs,
    ):
        super().__init__("POST", url, callback, data=data, json=json, **kwargs)
