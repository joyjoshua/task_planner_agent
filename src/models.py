from pydantic import BaseModel, Field
from typing import List, Optional

class Task(BaseModel):
    """
    Represents a single task in a plan.
    """
    id: int = Field(..., description="Unique identifier for the task")
    description: str = Field(..., description="Clear description of what needs to be done")
    priority: str = Field(..., description="Priority level: High, Medium, or Low")
    estimated_time: str = Field(..., description="Estimated time to complete (e.g., '30 mins')")
    status: str = Field("pending", description="Current status of the task")

class TaskPlan(BaseModel):
    """
    Represents a complete plan consisting of multiple tasks.
    """
    goal: str = Field(..., description="The original user goal")
    tasks: List[Task] = Field(..., description="List of steps to achieve the goal")
