from requests import Response as RqResponse
from urllib.parse import urljoin
from bs4 import BeautifulSoup as Bs


class Response:
    def __init__(self, response: RqResponse):
        self._response = response

    @property
    # TODO: 可以加一个缓存
    def soup(self):
        return Bs(self._response.content, "html.parser")
    
    def select(self, selector):
        return self.soup.select(selector)
    
    def find(self, selector):
        return self.soup.find(selector)
    
    def find_all(self, selector):
        return self.soup.find_all(selector)
    
    def select_one(self, selector):
        return self.soup.select_one(selector)
    


    def __getattr__(self, name):

        if not hasattr(self._response, name):
            return self.__getattribute__(name)
        else:
            return getattr(self._response, name)

    def __repr__(self):
        return f"<Response [{self.status_code}]>"

    def __str__(self):
        return f"<Response [{self.status_code}]>"

    def urljoin(self, url):
        return urljoin(self.url, url)
