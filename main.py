from requests import Response
from xpider import CONFIG, Spider, GetRq

CONFIG["headers"]["user_agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/58.0.3029.110 Safari/537.36"
)


class MySpider(Spider):
    def begin(self):
        print("MySqider Started!")
        yield GetRq("https://www.baidu.com", self.parse_baidu)
        yield GetRq("https://www.baidu.com", self.parse_baidu)
        print("MySqider Ended!")

    def parse_baidu(self, response: Response):
        print(response.text[:1000])
        print(response.status_code)


myspider = MySpider()
myspider.run()
