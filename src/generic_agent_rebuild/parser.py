import json


def parse_llm_response(response: str):

    try:
        parsed = json.loads(response)
        return parsed

    except json.JSONDecodeError:

        return {
            "type": "response",
            "content": response
        }