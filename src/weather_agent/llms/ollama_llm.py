from ollama import chat


class Ollama_Llm:
    def __init__(self):
        self.model = "llama3:latest"
    def analyze(self,prompt):
        print("-"*20)
        print("Analysis started...")
        response = chat(
            model = self.model,
            messages =[
                {
                    "role":"system",
                    "content":f"""
                                You are smart inteliigent journalist and your job is to summarize 
                                data, tempreture ,news and so on
                                Data to be summarized:
                                    {prompt}
                                - Awlays keep summary simple and small. 
                                - don' say Let me know if you'd like me to summarize anything else!
                                - Just summarize and return response.No extra
                                - also always provide one line suggestion based on your summary like summary plus your suggestion if you think so
                                - lastly summarise them in bullet points 
                                
                                """
                }
            ]
        )
        return response['message']['content']
    def enrich_text(self,prompt):
       
       
        response = chat(
            model = self.model,
            messages =[
                {
                    "role":"system",
                    "content":f"""
                                You are smart inteliigent content writer and your job is to rewrite content
                                for social media like instagram, twitter, facebook and linkedin. 
                               
                                Content to be rewritten:
                                    {prompt}
                                - Awlays rewrite professionally.
                                - Just rewirte and return response. nothing extra like let me know and anything like that
                                - always return enriched text. nothing extra
                                """
                }
            ]
        )
        return response['message']['content']
    def decide(self,prompt,user_input):
       
      
        response = chat(
        model=self.model,
        messages=[
            {
                "role": "system",
                "content": f"""
                You are a routing engine.

                Your job is ONLY to decide which tool should be called.
                
                if you don't find any matching tool then you return below tools becuase we will be searching the things on internet
                {{"tool":"search_query", "params":{{"query":{user_input}}}}}
                query could be any text that could be searched

               {prompt}
            
                Never answer the user's question.
                Never explain.
                Never use markdown.
                Return ONLY valid JSON and always see params mentioned above and return the format
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
        # print("hi",response['message']['content'])
        return response['message']['content']
