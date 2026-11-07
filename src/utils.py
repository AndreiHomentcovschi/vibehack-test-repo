def format_amount(cents: int, currency: str = "EUR") -> str:
    return f"{cents / 100:.2f} {currency}"


def slugify(text: str) -> str:
    return "-".join(text.lower().split())
