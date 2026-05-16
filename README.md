# Generic Agent Rebuild

Rebuilding the GenericAgent research paper from scratch as a learning-focused AI engineering project.

---

## Goal

The goal of this project is to deeply understand how modern AI agents work by implementing a simplified version step by step.

This project focuses on:

- AI agents
- memory systems
- tool calling
- context engineering
- SOP-based learning
- long-running workflows

---

## Inspiration

Paper:
**GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization**

Main idea from the paper:

> AI agents perform better when their context contains only high-value decision-relevant information.

Instead of endlessly increasing context size, the system focuses on:
- memory organization
- context compression
- reusable SOPs
- efficient tool usage

---

## Planned Features

### MVP
- CLI agent
- tool execution
- working memory
- session logging
- SOP storage
- basic memory layers

### Later Versions
- context compression
- memory retrieval
- browser tools
- reflection loop
- autonomous workflows

---

## Project Structure

```text
src/
memory/
docs/
progress/
tests/
examples/
```

---

## Current Status

Phase 1 — Research & Architecture

---

## Tech Stack

- Python
- OpenAI / Anthropic APIs
- SQLite / Markdown memory
- Typer CLI
- Pydantic

---

## Learning Philosophy

This is not a “perfect reproduction” project.

The goal is:
- learning deeply
- building publicly
- understanding architecture
- improving engineering skills
- documenting the full journey

---

## Build In Public

I’ll be posting regular updates while building this project:
- architecture decisions
- debugging
- implementation progress
- failures
- lessons learned

---

## Current Capabilities

The agent can currently:

- accept tasks through CLI
- register tools
- execute tools
- read files using a modular tool system

Example:

```bash
python -m src.generic_agent_rebuild.main "file_read: examples/sample.txt"
```

---


## Progress Log

- [x] Project setup
- [x] Initial architecture
- [x] CLI agent
- [x] Tool registry
- [x] First tool execution flow
- [ ] Memory manager
- [ ] SOP system
- [ ] Context compression