from .tools.file_read import FileReadTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "file_read": FileReadTool(),
        }

    def get_tool(self, tool_name: str):

        return self.tools.get(tool_name)

    def list_tools(self):

        return list(self.tools.keys())