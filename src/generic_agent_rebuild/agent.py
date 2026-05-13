from rich import print

from .tool_registry import ToolRegistry


class Agent:

    def __init__(self):

        self.tool_registry = ToolRegistry()

    def run(self, task: str):

        print("[cyan]Agent started[/cyan]")
        print(f"[yellow]Task:[/yellow] {task}")

        print("\n[blue]Available Tools:[/blue]")

        for tool_name in self.tool_registry.list_tools():
            print(f"- {tool_name}")

        response = self.think(task)

        print("\n[green]Final Response:[/green]")
        print(response)

    def think(self, task: str) -> str:

        return f"I understand the task: {task}"