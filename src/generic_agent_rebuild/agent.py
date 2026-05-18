from rich import print

from .llm.client import LLMClient
from .parser import parse_llm_response
from .tool_registry import ToolRegistry


class Agent:

    def __init__(self):

        self.tool_registry = ToolRegistry()
        self.llm = LLMClient()

    def run(self, task: str):

        print("[cyan]Agent started[/cyan]")
        print(f"[yellow]Task:[/yellow] {task}")

        response = self.think(task)

        print("\n[green]Final Response:[/green]")
        print(response)

    def think(self, task: str):

        tools_description = self.build_tools_prompt()

        prompt = f"""
You are an AI agent.

You have access to tools.

Available tools:
{tools_description}

Rules:
- Respond ONLY in valid JSON.
- Do not add explanations outside JSON.

Response formats:

Normal response:
{{
    "type": "response",
    "content": "your response"
}}

Tool call:
{{
    "type": "tool_call",
    "tool": "tool_name",
    "args": {{
        "key": "value"
    }}
}}

User task:
{task}
"""

        llm_response = self.llm.generate(prompt)

        print("\n[blue]Raw LLM Response:[/blue]")
        print(llm_response)

        parsed = parse_llm_response(llm_response)

        response_type = parsed.get("type")

        if response_type == "response":
            return parsed.get("content", "")

        if response_type == "tool_call":

            tool_name = parsed.get("tool")
            args = parsed.get("args", {})

            if not tool_name:
                return "Tool call missing tool name"

            if not isinstance(args, dict):
                return "Tool call args must be a JSON object"

            tool = self.tool_registry.get_tool(tool_name)

            if tool is None:
                return f"Tool not found: {tool_name}"

            try:
                result = tool.execute(**args)
            except TypeError as e:
                return f"Tool argument error: {str(e)}"

            return f"Tool Result:\n{result}"

        return "Unknown response type"

    def build_tools_prompt(self):

        descriptions = []

        for tool in self.tool_registry.tools.values():
            descriptions.append(
                f"""
Tool Name: {tool.name}
Description: {tool.description}
Required args:
- path: string, path to the file that should be read
"""
            )

        return "\n".join(descriptions)
