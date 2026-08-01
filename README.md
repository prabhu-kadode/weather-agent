# Weather Agent

A simple AI-powered weather agent built from scratch in Python to understand how AI agents work without relying on agent frameworks.

The project demonstrates:

* LLM integration using Gemini
* Tool registration and execution
* Weather API integration
* AI-driven tool selection
* Response synthesis from tool outputs

This project is intended for learning the core concepts behind AI agents before exploring frameworks like LangGraph, CrewAI, or PydanticAI.

# How to Run

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure Gemini API Key

Create a `.env` file in the project root and add:

```text
GEMINI_API_KEY=your_gemini_api_key
```
### if you don't have gemini api key then you can setup ollama locally.
```text
I have setup ollama locally and i am able to use it freely without bothering about 429 issue. Currently our code works with ollama. 
```

### 3. Run the application

```bash
uv run python -m weather_agent.main or uv run main.py
```

> If you're using the `src` layout, prefer `python -m weather_agent.main` over `uv run main.py`.

### 4. Example

```text
You: What's the weather in Hyderabad?

Agent: It is currently 29°C in Hyderabad with moderate humidity and light winds. Overall, the weather is pleasant.
```
