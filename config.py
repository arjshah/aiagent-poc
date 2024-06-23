"""
This module is responsible for setting up environment variables required by the application.
It ensures that all necessary API keys and other configurations are available to the application
at runtime. This includes keys for external services such as OpenAI and any other service APIs used.
"""

import os
from dotenv import load_dotenv

def set_environment():
    """
    Loads environment variables from a .env file at the project root.
    This ensures all necessary API keys and configurations are set without
    hardcoding them into the source code.
    """
    load_dotenv()  # This will load the variables from a .env file if present

    # Print to confirm the variables are set (optional, for debugging purposes)
    print("Environment Variables Set:")
    print("SERPER_API_KEY:", os.getenv("SERPER_API_KEY"))
    print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))