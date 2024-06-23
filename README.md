# AI Research Agent POC

This repository contains a Python application designed to automate the generation of a comprehensive market research report on the martial arts gym software industry. The application uses artificial intelligence agents to gather data, analyze trends, and compile findings into a detailed report.

## Project Overview

The purpose of this project is to demonstrate the capabilities of AI-driven research automation. Using a combination of AI agents from the `CrewAI` framework and OpenAI's language models, the system performs tasks such as data analysis, market trend identification, competitor profiling, and report writing. The final output is a professional-grade HTML report that provides insights into the martial arts gym software market.

## Features

- **Automated Research Agents**: Utilize different AI agents for specific research tasks such as market analysis, financial analysis, feature comparison, and more.
- **Concurrent Task Execution**: Leverages Python's `concurrent.futures` to manage asynchronous task execution.
- **Comprehensive Reporting**: Compiles detailed sections of the market research report based on the agents' findings.
- **HTML Report Generation**: Generates a well-formatted HTML document for the compiled research report.

## Repository Structure

- `config.py`: Sets up necessary environment variables and configurations.
- `agents.py`: Defines and configures the AI agents used for different aspects of market research.
- `task_manager.py`: Manages the scheduling and execution of research tasks.
- `report_writer.py`: Handles the compilation and writing of the market research report.
- `html_generator.py`: Produces the HTML output of the final market research report.
- `main.py`: The main script that orchestrates the entire process from initialization to final output.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system. You will also need to install the following packages:

```bash
pip install crewai langchain_openai python-dotenv