import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_google_api_key():
    """Retrieves the Google API key from environment variables."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")
    return api_key
