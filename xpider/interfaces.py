from typing import final, Generator
from abc import ABC, abstractmethod


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

    @final  # 防止被子类重写, 虽然代码不会报错, 但是类型检查器会有提示
    def run(self):
        """
        启动爬虫
        此函数不应该被用户重写
        """
        for xtask in self.begin():
            xtask.run()
