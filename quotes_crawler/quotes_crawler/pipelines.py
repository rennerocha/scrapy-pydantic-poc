from collections import defaultdict
from pydantic import ValidationError
from quotes_crawler.items import Quote


class QuotesItemValidationPipeline:
    def process_item(self, item, spider):
        try:
            Quote.validate(item)
        except ValidationError as err:
            item["_validation"] = defaultdict(list)
            for error in err.errors():
                field_name = "/".join(str(loc) for loc in error["loc"])
                item["_validation"][field_name] = error["msg"]
        return item
