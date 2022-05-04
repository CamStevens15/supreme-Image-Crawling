import scrapy


class RossSpider(scrapy.Spider):
    name = "ross"
    allowed_domains = ["www.twoinchbrush.com"]
    start_urls = ["http://www.twoinchbrush.com/"]

    def parse(self, response):
        filename = "ross.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"saved file{filename}")
