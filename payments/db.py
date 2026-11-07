PAID: set[str] = set()


def mark_invoice_paid(invoice_id: str) -> None:
    PAID.add(invoice_id)
