Summary
=======

This project is a proof of concept to verify how hard is to use [Pydantic](https://pydantic-docs.helpmanual.io/)
as an alternative to [Scrapy items](https://docs.scrapy.org/en/latest/topics/items.html).

Some benefits that we can try to achieve using Pydantic:

- Make it easier to define fixed structures to our items;
- Remove the need to cast numeric values returned as strings, as they are will
  be [coerced](https://pydantic-docs.helpmanual.io/#example) to ints or floats automatically;
- Easier to validate fields and easier to include new (and complex) validation rules using
  Python (and all its libraries)

Quotes Spider
=============

- Scraping quote from http://quotes.toscrape.com/
- `tags` is a nested field of another model so we can check how nested fields behave
- Two custom validations added to test custom validators:
  - Only items with `author` starting with letter `A` or `a`
  - Maximum of two `tags`

If data is not valid, a `_validation` key is added providing context to where the errors
are:

```
{'_validation': defaultdict(<class 'list'>,
                            {'author': "must starts with 'A' letter",
                             'idx': 'value is not a valid integer'}),
 'author': 'J.K. Rowling',
 'author_url': 'http://quotes.toscrape.com/',
 'idx': 'NaN',
 'quote': '“It is our choices, Harry, that show what we truly are, far more '
          'than our abilities.”',
 'tags': [{'idx': 0, 'tag': 'abilities'}, {'idx': 1, 'tag': 'choices'}]}
```