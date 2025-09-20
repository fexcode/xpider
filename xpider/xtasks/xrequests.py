import requests
import sys
from typing import Callable, Optional, Any
import time, random
from ..interfaces import XTask
from ..cfgs import GetConfig
from ..xlogger import LOGGER
from ..xresponses import Response
from ..xprocess import Process


if sys.version_info < (3, 10):
    CALLABLE = Callable[[Response], Any]
else:
    from typing import TypeAlias

    CALLABLE: TypeAlias = Callable[[Response], Any]


class Request(XTask):
    """
    内部类, 用于处理 requests 请求
    """

    def __init__(self, method: str, url: str, callback: CALLABLE, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs
        self.callback = callback

    def run(self) -> Response:
        interval = [int(i) for i in tuple(GetConfig("interval")())]
        interval = random.randint(*interval)
        LOGGER.info(f"请求间隔 {interval} 秒")
        time.sleep(interval)

        headers = GetConfig("headers")()

        LOGGER.info(f"请求方法 {self.method} | 请求URL:{self.url}")
        LOGGER.debug(f"请求头: {headers}")
        LOGGER.debug(f"请求参数: {self.kwargs}")
        LOGGER.debug(
            "requests.request(**"
            + str(
                dict(
                    method=self.method,
                    url=self.url,
                    headers=headers,
                    **self.kwargs,
                )
            )
            + ")"
        )

        response = Response(
            requests.request(
                method=self.method,
                url=self.url,
                headers=headers,
                **self.kwargs,
            )
        )

        proc = Process(self.callback)
        proc.run(response)

        return response


class GetRq(Request):
    """
    Get请求一个网址

    参数:
        url: 网址
        callback: 回调函数, 接收 Response 对象作为参数
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
