import scrapy
from rossimages.items import ImageItem


class RossSpider(scrapy.Spider):
    name = "ross"
    allowed_domains = ["www.twoinchbrush.com"]
    start_urls = ["http://www.twoinchbrush.com/all-paintings"]

    def parse(self, response):
        URL_PREFIX = "https://www.twoinchbrush.com"
        for source in response.xpath(
            "//a[not(@target='_blank')]//div[@class='progressive replace']/@data-img"
        ).getall():
            yield ImageItem(image_urls=[f"{URL_PREFIX}{source}"])

        # Recursively crawl the next page and parse the images.
        yield from response.follow_all(
            xpath="//ul[@class='pagination']//a[@rel='next']", callback=self.parse
        )
