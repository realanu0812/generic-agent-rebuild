from rich import print

from .tool_registry import ToolRegistry
from .llm.client import LLMClient


class Agent:

    def __init__(self):
        self.tool_registry = ToolRegistry()
        self.llm_client = LLMClient()

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

        prompt = f"""
        You are a helpful AI agent.

        User task:
        {task}

        Respond concisely.
        """

        response = self.llm_client.generate(prompt)

        return response