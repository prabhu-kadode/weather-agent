from ..llms.ollama_llm import Ollama_Llm


class Enrich_Text:
    def __init__(self):
        self.llm = Ollama_Llm()
    @property
    def name(self):
        return "enrich_text"
    @property
    def description(self):
        return "this is tool to enirch text or finetune or rewirte in better way for posting on social media"
    
    @property
    def parameters(self):
        return {
            "text": {
                "type": "string",
                "description": "Text is enriched"
            }
        }
    def execute(self,text):
        
        content = self.llm.enrich_text(text)
        
        return content