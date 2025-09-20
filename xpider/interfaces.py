from typing import final, Generator, Optional
from abc import ABC, abstractmethod
from .xresponses import Response
from .xerrors import SpiderStopped


class XTask(ABC):
    """
    xpider的任务抽象基类
    """

    def __init__(self): ...

    @abstractmethod
    def run(self):
        """
        运行任务
        """
        raise NotImplementedError("请实现 run 方法")


class Spider(ABC):
    """
    所有xpider爬虫的基类

    调用run方法可以启动爬虫
    用户层的爬虫入口函数是 begin 方法
    """

    def __init__(self): ...

    @abstractmethod
    def begin(self) -> Generator:
        """
        用户层的爬虫入口函数
        所有用户的爬虫都应该实现这个方法
        """
        raise NotImplementedError("请实现 begin 方法")

    def parse(self, response: Optional[Response], *args, **kwargs) -> Generator:
        """
        解析响应
        子类可以重写这个方法来实现自己的解析逻辑
        """
        ...

    def on_finish(self):
        """
        爬虫结束时调用
        """
        pass

    def stop(self, reason: str = ""):
        """
        停止爬虫
        """
        raise SpiderStopped(reason)

    @final  # 防止被子类重写, 虽然代码不会报错, 但是类型检查器会有提示
    def run(self):
        """
        启动爬虫
        此函数不应该被用户重写
        """
        try:
            for xtask in self.begin():
                xtask.run()
        except SpiderStopped as e:
            print(f"爬虫停止: {e}")
        finally:
            self.on_finish()
