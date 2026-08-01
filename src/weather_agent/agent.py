from tools.weather import Weather_Tool
from tools.calculator import Calculate
from tools.file_organizer import File_Organizer
from llms.llm import GeminiLLM
from llms.ollama_llm import Ollama_Llm

import json
class Weather_Agent:
    def __init__(self):
        self.llm = Ollama_Llm()
        

        self.tools = {
            "weather":Weather_Tool(),
            "calculate":Calculate(),
            "fileorganizer":File_Organizer()
        }
    def run(self,user_input):
        print('Thinking....!')
        data = json.loads(self.llm.decide(user_input))
   
        print(data)
        
 
       
        tool_name = data['tool']
        arguments = data['arguments']

        tool = self.tools[tool_name]
        response = tool.execute(**arguments)
        print(response)
        
        return 
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
