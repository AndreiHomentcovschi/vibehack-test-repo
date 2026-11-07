SYMBOLS = {"EUR": "€", "USD": "$", "GBP": "£", "RON": "lei"}


def format_amount(cents: int, currency: str = "EUR") -> str:
    symbol = SYMBOLS.get(currency)
    amount = f"{cents / 100:,.2f}"
    if symbol is None:
        return f"{amount} {currency}"
    return f"{amount} {symbol}" if currency == "RON" else f"{symbol}{amount}"


def slugify(text: str) -> str:
    return "-".join(text.lower().split())
