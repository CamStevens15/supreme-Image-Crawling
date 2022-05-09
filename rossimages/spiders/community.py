import scrapy
from rossimages.items import ImageItem


class CommunitySpider(scrapy.Spider):
    name = "community"
    allowed_domains = ["www.twoinchbrush.com"]
    start_urls = ["https://www.twoinchbrush.com/fanpaintings"]

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
