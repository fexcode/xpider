from rich import console


class Logger:
    """
    日志等级
    0: 全部
    1: info, warning, error, critical
    2: warning, error, critical
    3: error, critical
    4: critical
    """

    def __init__(self):
        self.log_level = 0

        self.console = console.Console()

    def debug(self, *message):
        if self.log_level <= 0:
            self.console.print(f"DEBUG|\t", *message)

    def info(self, *message):
        if self.log_level <= 1:
            self.console.print(f"INFO|\t[blue]{message}[/blue]")

    def warning(self, *message):
        if self.log_level <= 2:
            self.console.print(f"WARNING|\t[yellow]{message}[/yellow]")

    def error(self, *message):
        if self.log_level <= 3:
            self.console.print(f"ERROR|\t[red]{message}[/red]")

    def critical(self, *message):
        if self.log_level <= 4:
            self.console.print(f"CRITICAL|\t[bold red]{message}[/bold red]")


LOGGER = Logger()
