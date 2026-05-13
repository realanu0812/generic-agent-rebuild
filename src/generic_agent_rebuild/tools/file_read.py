from pathlib import Path

from .base import BaseTool


class FileReadTool(BaseTool):

    name = "file_read"
    description = "Reads contents of a file"

    def execute(self, path: str):

        file_path = Path(path)

        if not file_path.exists():
            return f"Error: File does not exist -> {path}"

        try:
            content = file_path.read_text()

            return content

        except Exception as e:
            return f"Error reading file: {str(e)}"