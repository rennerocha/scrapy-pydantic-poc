import scrapy
import random
from quotes_crawler.items import Quote, Tag


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for idx, quote in enumerate(response.css(".quote")):
            tags = []
            for tag_idx, tag in enumerate(quote.css(".tag *::text").getall()):
                tags.append(Tag.construct(**{"idx": tag_idx, "tag": tag}))

            item = Quote.construct(
                quote=quote.css(".text::text").get(),
                author=quote.css(".author::text").get(),
                author_url=response.urljoin(quote.css(".author a::attr(href)").get()),
                tags=tags,
                idx=idx,
            )
            yield item.dict()

        yield scrapy.Request(
            response.urljoin(response.css(".next a::attr(href)").get())
        )
