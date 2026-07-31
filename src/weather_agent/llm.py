import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiLLM:
    def __init__(self):
        self.client = genai.Client(api_key= os.getenv('GEMINI_API_KEY'))
    def decide(self,user_input):
        prompt = f"""
        You are an AI agent.

        Available tools:

        1. weather
        Description: Returns current weather for a city.

        Return ONLY valid JSON.

        Example:

        {{
        "tool": "weather",
        "arguments": {{
            "city": "Hyderabad"
        }}
        }}

        User: {user_input}
        """
                
        response = self.client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        )
        return response.text
    
    def response_synthesis(self,prompt):
        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )

        return response.text