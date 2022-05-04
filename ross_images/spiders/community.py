import scrapy


class CommunitySpider(scrapy.Spider):
    name = "community"
    allowed_domains = ["www.twoinchbrush.com"]
    start_urls = ["https://www.twoinchbrush.com/fanpaintings"]

    def parse(self, response):
        filename = "ross_community.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
