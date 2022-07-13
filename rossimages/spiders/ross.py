import scrapy
from rossimages.items import ImageItem


class RossSpider(scrapy.Spider):
    """This spider crawls original Ross paintings as well as fan recreations and saves them to a directory."""

    name = "ross"
    allowed_domains = ["www.twoinchbrush.com"]
    start_urls = [
        "https://www.twoinchbrush.com/all-paintings",
        "https://www.twoinchbrush.com/fanpaintings",
    ]

    def parse(self, response):
        URL_PREFIX = "https://www.twoinchbrush.com"
        image_urls = [
            f"{URL_PREFIX}{source}"
            for source in response.xpath(
                "//a[not(@target='_blank')]//div[@class='progressive replace']/@data-img"
            ).getall()
        ]
        yield ImageItem(image_urls=image_urls)

        # Recursively crawl the next page and parse the images.
        yield from response.follow_all(
            xpath="//ul[@class='pagination']//a[@rel='next']", callback=self.parse
        )
