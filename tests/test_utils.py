from src.utils import format_amount


def test_symbols():
    assert format_amount(1250, "EUR") == "€12.50"
    assert format_amount(123456, "USD") == "$1,234.56"
    assert format_amount(500, "RON") == "5.00 lei"


def test_unknown_currency_keeps_code():
    assert format_amount(100, "CHF") == "1.00 CHF"
