# src/api_client.py

import os
import openai
from openai import RateLimitError, APIError
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key=os.environ.get("SAMBANOVA_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://api.sambanova.ai/v1",
)

def get_completion(prompt, model_name, max_retries=3, delay=2):
    """Get completion from the API with retry logic."""
    retries = 0
    while retries <= max_retries:
        try:
            completion = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                temperature=0.1,
                top_p=0.1,
            )
            response_text = "".join(
                chunk.choices[0].delta.content or "" for chunk in completion
            )
            return response_text
        except RateLimitError:
            print("Rate limit exceeded. Retrying...")
            time.sleep(delay)
            retries += 1
        except APIError as e:
            print(f"API Error: {e}")
            retries += 1
            time.sleep(delay)
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise e
    raise Exception("Max retries exceeded.")
