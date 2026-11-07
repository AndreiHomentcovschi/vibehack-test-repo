PAID: set[str] = set()
ATTEMPTS: list[tuple[str, int]] = []


def mark_invoice_paid(invoice_id: str) -> None:
    PAID.add(invoice_id)


def record_attempt(event_id: str, attempt: int) -> None:
    ATTEMPTS.append((event_id, attempt))
