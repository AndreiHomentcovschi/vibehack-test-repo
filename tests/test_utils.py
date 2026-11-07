from src.utils import format_amount, slugify


def test_format_amount_default_currency():
    assert format_amount(1999) == "19.99 EUR"


def test_format_amount_custom_currency():
    assert format_amount(500, "USD") == "5.00 USD"


def test_slugify():
    assert slugify("Invoice Export Q3") == "invoice-export-q3"
