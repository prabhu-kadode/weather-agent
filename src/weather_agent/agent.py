import json

from llms.ollama_llm import Ollama_Llm
from tools.calculator import Calculate
from tools.file_organizer import File_Organizer
from tools.search_query import Search_Query
from tools.sumarry import Summary
from tools.weather import Weather_Tool
from weather_agent.tools.enrich_text import Enrich_Text


class Weather_Agent:
    def __init__(self):
        self.llm = Ollama_Llm()
        self.ENABLED_ANALYZE = False
        self.restricated_tools_for_analyze = ["calculator","fileorganizer"]
        self.tools = {
            "weather":Weather_Tool(),
            "calculator":Calculate(),
            "fileorganizer":File_Organizer(),
            "summary":Summary(),
            "search_query":Search_Query(),
            "enrich_text":Enrich_Text(),
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
        print('Thinking....!')
        
        data = json.loads(self.llm.decide(prompt,user_input))
        tool_name = data['tool']
        arguments = data['params']
        print(data)
        tool = self.tools[tool_name]
        response = tool.execute(**arguments)
        if tool_name in self.restricated_tools_for_analyze:
            return response
        return self.llm.analyze(response) if self.ENABLED_ANALYZE else response
       