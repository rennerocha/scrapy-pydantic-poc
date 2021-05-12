BOT_NAME = "quotes_crawler"

SPIDER_MODULES = ["quotes_crawler.spiders"]
NEWSPIDER_MODULE = "quotes_crawler.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "quotes_crawler.pipelines.QuotesItemValidationPipeline": 300,
}
