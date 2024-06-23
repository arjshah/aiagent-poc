"""
Defines the creation and configuration of various AI agents used throughout the application.
Each agent is designed to perform specific tasks related to market research, such as data analysis,
writing, or feature comparison. This module utilizes the CrewAI framework for defining agent roles
and capabilities.
"""

from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

def create_agent(role, goal, model="gpt-3.5-turbo-16k"):
    return Agent(
        role=role,
        goal=goal,
        verbose=True,
        memory=True,
        backstory=f"You are a senior {role.lower()} with over 20 years of experience in the software industry, specializing in martial arts and fitness tech markets.",
        tools=[search_tool],
        llm=ChatOpenAI(model=model, temperature=0.7)
    )