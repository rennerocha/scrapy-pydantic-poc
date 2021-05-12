from pydantic import BaseModel, ValidationError, validator
from typing import List


class Tag(BaseModel):
    idx: int
    tag: str


class Quote(BaseModel):
    idx: int
    quote: str
    author: str
    author_url: str
    tags: List[Tag]

    @validator("author")
    def author_must_start_with_a(cls, value):
        if not value.startswith("A") and not value.startswith("a"):
            raise ValueError("must starts with 'A' letter")
        return value

    @validator("tags")
    def only_two_tags_allowed(cls, value):
        if len(value) > 2:
            raise ValueError("only two tags allowed")
        return value
