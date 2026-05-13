from rich import print


class Agent:

    def run(self, task: str):
        print(f"[cyan]Agent started[/cyan]")
        print(f"[yellow]Task:[/yellow] {task}")

        response = self.think(task)

        print(f"[green]Final Response:[/green]")
        print(response)

    def think(self, task: str) -> str:
        """
        Placeholder reasoning step.

        Later this will call:
        - LLM
        - tools
        - memory
        """

        return f"I understand the task: {task}"