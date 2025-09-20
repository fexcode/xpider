from typing import Any, Generator
from xpider import CONFIG, Spider, GetRq, Response

print(CONFIG)
CONFIG["headers"]["referer"] = "https://cn.bing.com/"


class MySpider(Spider):
    def __init__(self):
        super().__init__()
        self.url = "https://movie.douban.com/top250/"

    def begin(self) -> Generator[GetRq, Any, None]:
        print("开始爬取: ", self.url)
        yield GetRq(self.url, self.parse)

    def parse(self, response: Response):
        # 获取本页电影名
        names = response.select("div.hd > a > span.title")
        for item in names:
            self.adddata(item.get_text())

        # 跟进下一页
        next = response.select_one("span.next > link")
        if not next:
            self.stop("没有下一页了")
            return
        else:
            next = next["href"]

        next = response.urljoin(next)

        print("跟进下一页: ", next)
        yield GetRq(next, self.parse)

    def on_finish(self):
        self.save("result.txt")


myspider = MySpider()
myspider.run()
