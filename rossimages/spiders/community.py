import scrapy


class CommunitySpider(scrapy.Spider):
    name = "community"
    allowed_domains = ["www.twoinchbrush.com"]
    start_urls = ["https://www.twoinchbrush.com/fanpaintings"]

    def parse(self, response):
        filename = "community.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")

        # Recursively crawl the next page and parse the images.
        # yield from response.follow_all(
        #     xpath="ul[@class='pagination']//a[@rel='next']", callback=self.parse
        # )
