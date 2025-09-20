from requests import Response as RqResponse
from urllib.parse import urljoin


class Response:
    def __init__(self, response: RqResponse):
        self._response = response

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
