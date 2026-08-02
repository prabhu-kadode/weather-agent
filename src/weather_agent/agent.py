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
            "calculator":Calculate(),
            "fileorganizer":File_Organizer()
        }
    def build_tool_prompt(self):

        prompt = "Available tools:\n\n"

        for tool in self.tools.values():

            prompt += f"Tool: {tool.name}\n"
            prompt += f"Description: {tool.description}\n"
            prompt += "Parameters:\n"

            for name, info in tool.parameters.items():

                prompt += f"- {name}: {info}\n"

            prompt += "\n"
         
       

        return prompt
    def run(self,user_input):
        prompt = self.build_tool_prompt()
        print('Thinking....!',prompt)
        
        
        data = json.loads(self.llm.decide(prompt,user_input))
        tool_name = data['tool']
        arguments = data['params']

        tool = self.tools[tool_name]
        response = tool.execute(**arguments)
        print(response)
        return response