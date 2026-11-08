PAID: set[str] = set()
ATTEMPTS: list[tuple[str, int]] = []


def mark_invoice_paid(invoice_id: str) -> None:
    PAID.add(invoice_id)


def record_attempt(event_id: str, attempt: int) -> None:
    ATTEMPTS.append((event_id, attempt))


import random


def backoff_seconds(attempt: int, base: float = 0.5) -> float:
    """Exponential backoff with full jitter."""
    return random.uniform(0, base * 2 ** attempt)
