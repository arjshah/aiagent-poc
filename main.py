import atexit
from config import set_environment

# Set environment variables and initialize agents
set_environment()

from crewai import Task
from agents import create_agent
from task_manager import execute_task
from report_writer import compile_section
from html_generator import generate_html
import os
import psutil
import threading

# Counter to keep track of running tasks
task_counter = threading.Semaphore(0)

# Define agents
researcher = create_agent("Market Researcher", "Conduct in-depth, data-driven research on the martial arts gym software market", model="gpt-3.5-turbo")
analyst = create_agent("Market Analyst", "Provide detailed analysis of market data, trends, and competitive landscape in martial arts gym software", model="gpt-3.5-turbo")
feature_specialist = create_agent("Product Specialist", "Analyze and compare specialized features of martial arts gym software products", model="gpt-3.5-turbo")
financial_analyst = create_agent("Financial Analyst", "Analyze pricing strategies, business models, and financial aspects of the martial arts gym software market", model="gpt-3.5-turbo")
writer = create_agent("Senior Research Writer", "Compile and write a comprehensive, professional-grade market research report", model="gpt-3.5-turbo")

# Define research tasks
research_tasks = [
    Task(
        description="Conduct a thorough analysis of the martial arts gym software market size. Include current valuation, historical growth rates, and detailed future projections. Break down the market size by region, software type, and end-user segments. Provide specific numbers and cite sources.",
        expected_output='A detailed market size analysis with specific figures, growth rates, and segment breakdowns.',
        agent=researcher
    ),
    Task(
        description="Identify and profile the top 10 competitors in the martial arts gym software market. For each competitor, provide company background, key products, market share, revenue figures (if available), unique selling propositions, and recent developments. Analyze their strengths and weaknesses.",
        expected_output='In-depth profiles of top 10 competitors with SWOT analysis.',
        agent=analyst
    ),
    Task(
        description="Analyze current market trends in martial arts gym software. Include technological advancements, shifting customer preferences, and emerging business models. Provide specific examples and case studies to illustrate each trend. Quantify the impact of these trends where possible.",
        expected_output='Detailed analysis of 5-7 major market trends with supporting data and case studies.',
        agent=analyst
    ),
    Task(
        description="Conduct a comprehensive analysis of pricing strategies and business models in the martial arts gym software market. Include a breakdown of different pricing tiers, comparison of subscription vs. one-time purchase models, and analysis of freemium strategies. Provide specific pricing examples from leading companies.",
        expected_output='Detailed pricing analysis with specific examples and comparative data.',
        agent=financial_analyst
    ),
    Task(
        description="Research and analyze specialized features in martial arts gym software. Identify unique features tailored specifically for martial arts gyms, their implementation across different software products, and their effectiveness. Provide specific examples and compare top products.",
        expected_output='Comprehensive analysis of specialized martial arts software features with product comparisons.',
        agent=feature_specialist
    )
]

def cleanup():
    print("Cleaning up resources...")

    # Close any open files
    print("Closing open files...")
    for proc in psutil.Process().children(recursive=True):
        try:
            for file in proc.open_files():
                os.close(file.fd)
        except Exception as e:
            print(f"Error closing file: {e}")

    # Release any held resources (e.g., database connections, network sockets)
    print("Releasing held resources...")
    # Add your resource release code here

    # Perform any additional cleanup tasks specific to your application
    print("Performing additional cleanup tasks...")
    # Add your additional cleanup code here

    print("Cleanup completed.")

def worker_thread(task):
    try:
        task_counter.acquire()
        result = execute_task(task)
        # Process the result
        return (task.description, result)
    except Exception as exc:
        print(f"Task {task.description[:50]}... generated an exception: {exc}")
        # Handle the exception gracefully
        return (task.description, None)
    finally:
        task_counter.release()

def run_tasks():
    threads = []
    for task in research_tasks:
        thread = threading.Thread(target=worker_thread, args=(task,))
        thread.start()
        threads.append(thread)
        task_counter.release()

    # Wait for all tasks to complete
    for _ in range(len(research_tasks)):
        task_counter.acquire()

    # Wait for all worker threads to finish
    for thread in threads:
        thread.join()

    # Collect the results from the worker threads
    results = []
    for thread in threads:
        result = thread.join()
        if result is not None:
            results.append(result)

    formatted_results = [
        {'description': task_name, 'input_data': result}
        for task_name, result in results
    ]
    
    compiled_research = compile_section("Complete Market Analysis", formatted_results)
    
    # Generate HTML report
    html_content = generate_html(compiled_research)
    
    # Write HTML output to file
    html_file_path = "comprehensive_martial_arts_software_market_report.html"
    with open(html_file_path, "w") as file:
        file.write(html_content)
    print(f"HTML report has been generated and saved to {html_file_path}")

def main():
    try:
        run_tasks()
        print("Script execution completed.")
    except KeyboardInterrupt:
        print("Script execution interrupted by the user.")
    finally:
        cleanup()

if __name__ == "__main__":
    atexit.register(cleanup)
    main()