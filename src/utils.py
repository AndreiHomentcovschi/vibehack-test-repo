def format_amount(cents: int, currency: str = "EUR") -> str:
    return f"{cents / 100:.2f} {currency}"


def slugify(text: str) -> str:
    return "-".join(text.lower().split())


def invoice_number(sequence: int, year: int, prefix: str = "INV") -> str:
    """INV-2026-00042 style invoice numbers."""
    if sequence < 1:
        raise ValueError("sequence starts at 1")
    return f"{prefix}-{year}-{sequence:05d}"
