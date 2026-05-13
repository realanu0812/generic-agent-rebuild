# Architecture

This project is a simplified rebuild of GenericAgent.

The goal is not to fully reproduce the paper.

The goal is to build a practical learning-focused agent with:

- simple CLI interface
- tool calling
- working memory
- long-term memory
- SOP generation
- context management

## Core Idea

The agent should not keep everything in context.

Instead, it should keep only the most useful information active and store the rest in structured memory.

## MVP Architecture

User Task
→ CLI
→ Agent Loop
→ LLM
→ Tool Calls
→ Tool Results
→ Working Memory Update
→ Final Answer
→ Optional SOP / Memory Update

## Main Components

### 1. CLI

Accepts user tasks from the terminal.

Example:

```bash
python -m generic_agent_rebuild "summarize this file"