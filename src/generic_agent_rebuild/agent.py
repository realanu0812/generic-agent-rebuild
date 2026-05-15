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
        """
        Very simple temporary decision logic.

        Later, the LLM will decide:
        - whether a tool is needed
        - which tool to call
        - what arguments to pass
        """

        if task.startswith("file_read:"):
            path = task.replace("file_read:", "").strip()

            tool = self.tool_registry.get_tool("file_read")

            if tool is None:
                return "Error: file_read tool is not available."

            result = tool.execute(path=path)

            return f"Tool Result:\n{result}"

        return f"I understand the task: {task}"