# AI Agent

A simple AI Agent built from scratch in Python to understand how AI agents work without relying on agent frameworks.

The goal of this project is to learn the fundamentals of AI agents by implementing every component ourselves instead of depending on libraries such as LangChain, CrewAI, LangGraph, or PydanticAI.

## Features

* LLM integration (Ollama/Gemini)
* Tool registration and execution
* AI-driven tool selection
* Response synthesis
* Modular and extensible architecture
* Easily add new tools without changing the agent logic

## Available Tools

* 🌤️ Weather Tool – Get the current weather for any city using the Open-Meteo API.
* 🧮 Calculator Tool – Perform basic mathematical calculations.
* 📁 File Organizer Tool – Organize files into folders based on their extensions.

## Project Structure

The project is designed around the following components:

* **Agent** – Coordinates the overall workflow.
* **LLM** – Decides which tool to invoke and generates the final response.
* **Tool Registry** – Registers all available tools.
* **Tools** – Perform specific tasks such as weather lookup, calculations, or file organization.

## Learning Objectives

This project demonstrates:

* Building an AI agent from scratch
* Prompt engineering
* Tool calling architecture
* External API integration
* Local LLM integration with Ollama
* Clean project architecture
* Extensible tool framework

---

# How to Run

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure the LLM

#### Option 1: Ollama (Recommended)

Install Ollama and pull a model:

```bash
ollama pull llama3
```

Ensure the Ollama server is running before starting the application.

#### Option 2: Gemini

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

> **Note:** The current implementation uses Ollama by default. Gemini support can be enabled by switching the LLM implementation.

### 3. Run the application

```bash
uv run python -m weather_agent.main
```

or

```bash
uv run main.py
```

> If you're using the `src` layout, prefer `uv run python -m weather_agent.main`.

---

# Example

```text
You: What's the weather in Hyderabad?

Agent: It is currently 29°C in Hyderabad with moderate humidity and light winds.
```

```text
You: Calculate 245 + 873

Agent: The result is 1118.
```

```text
You: Organize my Downloads folder.

Agent: Successfully organized your files into categorized folders based on their file extensions.
```

## Future Enhancements

* Native tool calling
* Memory support
* Multi-step planning
* Web search tool
* Git tool
* Read/Write file tools
* Shell command execution
* RAG integration
* MCP server integration
