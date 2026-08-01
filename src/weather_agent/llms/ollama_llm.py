from ollama import chat

class Ollama_Llm:
    def __init__(self):
        self.model = "llama3:latest"
    def decide(self,prompt,user_input):
       
      
        response = chat(
        model=self.model,
        messages=[
            {
                "role": "system",
                "content": f"""
                You are a routing engine.

                Your job is ONLY to decide which tool should be called.

               {prompt}
            
                Never answer the user's question.
                Never explain.
                Never use markdown.
                Return ONLY valid JSON.
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
        print("hi",response['message']['content'])
        return response['message']['content']
