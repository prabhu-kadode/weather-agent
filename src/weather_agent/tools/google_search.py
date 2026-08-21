import os
import requests

from interface.search import Search

from bs4 import BeautifulSoup
class Google_Search(Search):
    def __init__(self):
        self.url = "https://www.google.com/search"
        self.API_KEY = os.getenv('GEMINI_API_KEY')
        self.GOOGLE_ID = os.getenv('GOOGLE_ID')
    def search(self,query):
        params = {
        "q": query
        }
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(self.url, params=params,headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        for link in soup.select("a"):
            href = link.get("href")
            print("HREF:", href)

        return None

       
    def get_page_content(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove things that aren't useful for summarization
        for element in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "aside"
        ]):
            element.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text