from llms.ollama_llm import Ollama_Llm


class Summary:
    def __init__(self):
        self.llm = Ollama_Llm()

    @property
    def name(self):
        return "summary"

    @property
    def description(self):
        return "This tool is used to summarise the text"

    @property
    def parameters(self):
        return {
            "text_summary": {
                "type": "string",
                "description": "Text that needs to be sumarised",
            }
        }

    def execute(self, text_summary):
        print("-" * 10)
        print("Summary of text\n")
        print(text_summary)
        print("-" * 10)
        return text_summary
