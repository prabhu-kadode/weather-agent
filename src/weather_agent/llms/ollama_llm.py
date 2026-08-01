from ollama import chat

class Ollama_Llm:
    def __init__(self):
        self.model = "llama3:latest"
    def decide(self,user_input):
       
      
        response = chat(
        model=self.model,
        messages=[
            {
                "role": "system",
                "content": """
                You are a routing engine.

                Your job is ONLY to decide which tool should be called.

                Available tools:

                1. weather(city)
                2. calculate(a, b)
                3. fileorganizer(target,action)

               Return one of these JSON objects only.

                Weather:

                {
                "tool": "weather",
                "arguments": {
                    "city": "Delhi"
                }
                }

                Calculator:

                {
                "tool": "calculate",
                "arguments": {
                    "a": 10,
                    "b": 20
                }
                }

                Fileorganizer:

                {
                "tool": "fileorganizer",
                "arguments": {
                    "target":"downloads",
                    "action": "move"
                }
                }
                Target rules:
                Action rules:
                - Target could be any folder name 
                  examples: downloads, documents, and so on. 

                - Use "move" when the user wants to organize, sort, categorize, or arrange files.
                - Use "delete" only when the user explicitly asks to remove, delete, erase, or permanently discard files.
            
                Never answer the user's question.
                Never explain.
                Never use markdown.
                Never wrap the JSON in ``` blocks.
                """
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ],
                    options={
                        "temperature": 0
                    }
            )
        print(response['message']['content'])
        return response['message']['content']
