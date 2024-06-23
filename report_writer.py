"""
Responsible for writing the sections of the market research report based on input from various agents.
It formats the findings into a coherent report, structuring it into sections like executive summary,
market analysis, and competitive landscape. This module generates the content for the final report,
ensuring professional quality and clarity.
"""

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from agents import create_agent

# Assuming the writer agent needs to be defined here as it was not shown in agents.py.
# You can adjust the model or parameters as needed.
writer_agent = create_agent("Senior Research Writer", "Compile and write a comprehensive, professional-grade market research report", model="gpt-4")

def write_subsection(description, input_data):
    """
    Creates a task to write a specific subsection of the market research report.
    Each subsection handles a part of the section, allowing detailed and focused content generation.
    """
    task = Task(
        description=description,
        expected_output='A well-articulated, detailed subsection of the market research report.',
        agent=writer_agent,
        async_execution=True # Asynchronous execution to manage complex content generation
    )
    crew = Crew(
        agents=[writer_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=2
    )
    result = crew.kickoff()
    return str(result)  # Convert the result to a string

def compile_section(section_name, subsections):
    """
    Orchestrates the writing of multiple subsections to compile a complete section of the report.
    This function aggregates the results of each subsection into a single section.
    """
    section_content = []
    for subsection in subsections:
        description = subsection['description']
        input_data = subsection['input_data']
        content = write_subsection(description, input_data)
        section_content.append(content)
    return "\n\n".join(section_content)

def main():
    market_overview_subsections = [
        {
            "description": "Analyze the current market size and its components for martial arts gym software.",
            "input_data": "Data regarding current market size including user base and revenue streams."
        },
        {
            "description": "Discuss historical growth rates and project future trends in the martial arts gym software market.",
            "input_data": "Historical data and future projections of market growth rates."
        },
        {
            "description": "Break down the market by regions and segments specifically tailored to martial arts gyms.",
            "input_data": "Market segmentation data by region and type of martial arts gyms."
        }
    ]
    market_overview = compile_section("Market Overview and Size", market_overview_subsections)
    return market_overview

if __name__ == "__main__":
    compiled_section = main()
    print("Compiled Market Overview Section:\n", compiled_section)