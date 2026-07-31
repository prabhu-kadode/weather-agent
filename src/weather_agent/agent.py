from weather import Weather_Tool
from llm import GeminiLLM
import json
class Weather_Agent:
    def __init__(self):
        self.llm = GeminiLLM()

        self.tools = {
            "weather":Weather_Tool()
        }
    def run(self,user_input):
        data = json.loads(self.llm.decide(user_input))
        print(data)
        tool_name = data['tool']
        arguments = data['arguments']

        tool = self.tools[tool_name]
        response = tool.execute(**arguments)
        print(response)
        

        prompt = f"""
        You are a helpful AI assistant.

        The requested tool has already been executed.

        Your task is to answer the user's question using ONLY the tool result provided below.

        Instructions:
        - Do not mention the tool or API.
        - Do not invent or assume any information.
        - If the tool result is missing information, say so politely.
        - Keep the answer concise and natural.
        - If appropriate, provide a helpful recommendation based on the weather.
        - also mention city name and tempreture in proper format

        User Question:
        {user_input}

        Tool Result:
        {response}
        """

        print(self.llm.response_synthesis(prompt))
