from .reddit_search import Reddit_Search


class Search_Query:
    def __init__(self):
        self.search_engine = Reddit_Search()
    @property
    def name(self):
        return "search_query"
    @property
    def description(self):
        return "This is tool to search query from internet"
    @property
    def parameters(self):
        return {
            "query":{
                "type":"string",
                "description":"Text that needs to be searched on google"

            }
        }
    def execute(self,query):
        first_link = self.search_engine.search(query)
        print(first_link)
        
        return "query"
