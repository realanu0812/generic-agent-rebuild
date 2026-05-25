from pyexpat.errors import messages
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

        messages = [
        {
        "role": "user",
        "content": task
        }
                    ]

        response = self.run_agent_loop(messages)

        print("\n[green]Final Response:[/green]")
        print(response)

    def run_agent_loop(self, messages):

        max_steps = 5

        for step in range(max_steps):

            print(f"\n[magenta]Agent Step {step + 1}[/magenta]")

            response = self.think(messages)

            if response["type"] == "response":
                return response["content"]

            if response["type"] == "tool_call":

                tool_name = response["tool"]
                args = response["args"]

                tool = self.tool_registry.get_tool(tool_name)

                if tool is None:
                    return f"Tool not found: {tool_name}"

                try:
                    result = tool.execute(**args)

                except Exception as e:
                    result = f"Tool execution error: {str(e)}"

                print(f"\n[blue]Tool Executed:[/blue] {tool_name}")

                print(f"\n[yellow]Tool Result:[/yellow]")
                print(result)

                messages.append({
                    "role": "assistant",
                    "content": str(response)
                })

                messages.append({
                    "role": "user",
                    "content": f"Tool result:\n{result}"
                })

        return "Agent stopped: max steps reached"

    def think(self, messages):

        tools_description = self.build_tools_prompt()

        prompt = f"""
You are an AI agent.

You have access to tools.

Available tools:
{tools_description}

Rules:
- Respond ONLY in valid JSON.
- Do not add explanations outside JSON.
- If the task is complete, return a normal response.
- If you need external information, use a tool.

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

Conversation:
{messages}
"""

        llm_response = self.llm.generate(prompt)

        print("\n[blue]Raw LLM Response:[/blue]")
        print(llm_response)

        parsed = parse_llm_response(llm_response)

        response_type = parsed.get("type")

        if response_type == "response":
            return parsed

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

            return parsed

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
