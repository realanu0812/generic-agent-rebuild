import typer
from rich import print

app = typer.Typer()


@app.command()
def run(task: str):
    print(f"[green]Received task:[/green] {task}")


if __name__ == "__main__":
    app()