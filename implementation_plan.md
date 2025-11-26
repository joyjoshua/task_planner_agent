# Task Planner Agent - Implementation Plan

This document outlines the step-by-step plan to build your **Task Planner Agent** for the Hackathon. It follows the "5 Days of AI" curriculum structure.

## Phase 1: Core Agent Architecture (The Brain)
**Goal**: Create an agent that can take a user request and break it down into a structured JSON plan.

*   [ ] **Step 1.1: Define the Data Model**
    *   Create a Pydantic model or a clear JSON schema for a `Task`.
    *   *Example*: `{"id": 1, "title": "Buy groceries", "priority": "High", "status": "pending"}`
*   [ ] **Step 1.2: Enhance `TaskPlannerAgent`**
    *   Update `src/agent.py` to use **System Instructions**.
    *   Teach the agent to output *only* JSON (using Gemini's structured output mode or careful prompting).
*   [ ] **Step 1.3: Basic Interaction Loop**
    *   Update `main.py` to parse the JSON response and display it prettily.

## Phase 2: Tools & Capabilities (The Hands)
**Goal**: Give the agent the ability to interact with the outside world (files, time, etc.).

*   [ ] **Step 2.1: Implement `BaseTool`**
    *   Ensure `src/tools/base.py` is robust.
*   [ ] **Step 2.2: Create `FileTool`**
    *   Create `src/tools/file_tool.py`.
    *   *Capability*: Read and write task lists to a file (e.g., `data/tasks.json`).
*   [ ] **Step 2.3: Create `TimeTool`**
    *   Create `src/tools/time_tool.py`.
    *   *Capability*: Get the current date/time (crucial for planning deadlines).
*   [ ] **Step 2.4: Tool Binding**
    *   Connect these tools to the Gemini model so it knows it can call them.

## Phase 3: Memory & Persistence (The Memory)
**Goal**: Make the agent remember past conversations and tasks.

*   [ ] **Step 3.1: Short-term Memory (Chat History)**
    *   Implement `src/memory/chat_memory.py`.
    *   Pass previous messages to the model in each turn.
*   [ ] **Step 3.2: Long-term Memory (Task Database)**
    *   Use `data/tasks.json` as the "database".
    *   Ensure the agent checks this file before creating new tasks (to avoid duplicates).

## Phase 4: Observability & Evaluation (The Eyes)
**Goal**: Understand *why* the agent made a decision and ensure it works reliably.

*   [ ] **Step 4.1: Structured Logging**
    *   Add print statements (or a logger) that show: `[THOUGHT]`, `[ACTION]`, `[OBSERVATION]`.
    *   This helps you debug when the agent gets confused.
*   [ ] **Step 4.2: Evaluation Script**
    *   Create `tests/test_agent.py`.
    *   Run a set of standard prompts (e.g., "Plan a birthday party") and check if the output JSON is valid.

## Phase 5: Multi-Agent Collaboration (The Team)
**Goal**: Split responsibilities for better performance.

*   [ ] **Step 5.1: The Planner**
    *   Specializes in breaking high-level goals into steps.
*   [ ] **Step 5.2: The Executor**
    *   Specializes in taking one step and doing it (e.g., "Send the invite email").
*   [ ] **Step 5.3: Orchestrator**
    *   A main loop that passes data between the Planner and Executor.

---

## Getting Started
Start with **Phase 1**. Do not try to build everything at once!
