from urllib.parse import quote

import httpx

from interface.search import Search


class Reddit_Search(Search):
    def __init__(self):
        pass

    def search(self, query):
        encoded_query = quote(query)
        url = f"https://www.reddit.com/search.json?q=${encoded_query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = httpx.get(url, headers=headers)
        print("hello" * 10)
        print(response.status_code)

        print(response.json())
        return "text"

    def get_page_content(self, url):
        pass
