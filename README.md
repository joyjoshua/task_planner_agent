# Task Planner Agent

This is a scaffold project for building a Task Planner Agent using the Google Generative AI SDK (Gemini).

## Project Structure

```
task_planner_agent/
├── .env.example       # Template for environment variables
├── .gitignore         # Git ignore rules
├── data/              # Directory for database files and persistent storage
├── main.py            # Entry point of the application
├── requirements.txt   # Python dependencies
├── src/               # Source code directory
│   ├── __init__.py
│   ├── agent.py       # Agent logic and Google SDK integration
│   ├── config.py      # Configuration and secret management
│   ├── memory/        # Agent memory management
│   │   ├── __init__.py
│   │   └── base.py    # Base class for memory
│   └── tools/         # Agent tools and capabilities
│       ├── __init__.py
│       └── base.py    # Base class for tools
└── README.md          # Project documentation
```

## Setup

1.  **Install Python**: Ensure you have Python installed (3.9+ recommended).

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Secrets**:
    *   Copy `.env.example` to a new file named `.env`.
    *   Open `.env` and replace `your_api_key_here` with your actual Google API Key.
    *   You can get an API key from [Google AI Studio](https://aistudio.google.com/).

## Usage

Run the agent:

```bash
python main.py
```

Enter a goal when prompted, and the agent will generate a plan for you.

## Next Steps

*   Explore `src/agent.py` to customize the prompt and agent behavior.
*   Add more capabilities to the agent (e.g., saving plans to a file, integrating with other tools).
