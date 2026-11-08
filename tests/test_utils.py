from src.utils import format_amount


def test_symbols():
    assert format_amount(1250, "EUR") == "€12.50"
    assert format_amount(123456, "USD") == "$1,234.56"
    assert format_amount(500, "RON") == "5.00 lei"


def test_unknown_currency_keeps_code():
    assert format_amount(100, "CHF") == "1.00 CHF"


def test_invoice_number_pads_and_prefixes():
    from src.utils import invoice_number
    assert invoice_number(1, 2026) == "INV-2026-00001"
    assert invoice_number(123456, 2026) == "INV-2026-123456"
    assert invoice_number(7, 2026, prefix="CN") == "CN-2026-00007"
