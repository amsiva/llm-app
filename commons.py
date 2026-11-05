from openrouter import OpenRouter
from dotenv import load_dotenv
load_dotenv()
import os
import anthropic 

api_key = os.getenv("OPENROUTER_API_KEY")
client = OpenRouter(api_key=api_key)


def client_connection():
    client = anthropic.Anthropic(auth_token=api_key, base_url="https://openrouter.ai/api")
    return client