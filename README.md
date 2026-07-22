# Simple Chatbot 🤖

An AI-powered chatbot built with **Python, LangChain, and LangGraph**. This project uses an OpenAI language model with a ReAct agent to understand user requests and decide when additional tools are needed to complete a task.

## Features ✨

- 💬 Interactive command-line AI assistant
- 🧠 AI agent powered by LangChain + LangGraph
- 🔧 Dynamic tool usage when necessary
- 👋 Greeting tool for user interactions
- ➕ Addition calculations
- ➖ Subtraction calculations
- ✖️ Multiplication calculations
- ➗ Division calculations
- 🔄 Real-time response streaming

## How It Works ⚙️

The chatbot uses a **ReAct AI agent**, which allows the model to reason about user requests and determine the best action.

The agent can:
- Respond directly to normal conversations
- Use available tools when a task requires additional functionality
- Return the tool results as part of its final response

Example:

```
User: Hello

Agent: Responds normally with a conversation.


User: What is 25 × 4?

Agent: Uses the multiplication tool and returns the result.
```

The workflow:

```
User Input
     ↓
AI Agent
     ↓
Decision:
     ├── Normal Response
     │
     └── Use Tool
            ↓
       Tool Result
            ↓
       Final Answer
```

## Technologies Used 🛠️

- Python
- LangChain
- LangGraph
- OpenAI API
- python-dotenv
- uv package manager

## Project Structure 📁

```
Simple Chatbot/
│
├── main.py              # Chatbot application
├── .env                 # API keys and environment variables
├── pyproject.toml       # Project dependencies
├── uv.lock              # Locked dependencies
└── README.md            # Documentation
```

## Setup 🚀

### Install Dependencies

Using uv:

```bash
uv sync
```

### Configure API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### Run the Chatbot

```bash
uv run main.py
```

## Available Tools 🔧

The chatbot currently has access to:

| Tool | Purpose |
|---|---|
| Greeting | Creates personalized greetings |
| Addition | Performs addition calculations |
| Subtraction | Performs subtraction calculations |
| Multiplication | Performs multiplication calculations |
| Division | Performs division calculations |

The AI agent decides when to use these tools based on the user's request.

## Future Improvements 🚧

- Add conversation memory
- Add more AI tools
- Add web search capabilities
- Add document analysis
- Build a web-based interface
- Deploy as an AI application

## Author

Kesley Abakabawakow

---

Built as a learning project exploring AI agents, tool calling, and LLM applications.
