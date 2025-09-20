from .interfaces import XTask
from typing import Generator, Callable

class Process:
    def __init__(self, fun: Callable[..., Generator]):
        self.fun = fun
        self.data = []

    def run(self, *args, **kwargs):
        for task in self.fun(*args, **kwargs):
            if isinstance(task, XTask):
                task.run()
