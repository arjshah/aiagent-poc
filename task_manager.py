"""
Manages the execution of tasks assigned to different agents. It handles task scheduling, execution,
and result collection using concurrent executions. This module ensures that all tasks are completed
successfully and aggregates the results for further processing.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from agents import create_agent
from crewai import Crew, Process, Task

def execute_task(task):
    try:
        result = task.agent.execute_task(task)
        return result.output.raw_output if result and result.output else None
    except Exception as e:
        return "Error: " + str(e)  # Handle errors by capturing them as strings
