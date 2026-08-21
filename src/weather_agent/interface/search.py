from abc import ABC, abstractmethod

class Search(ABC):

    @abstractmethod
    def get_page_content(self,url):
        pass
    @abstractmethod
    def search(self,url):
        pass