import time

from payments.db import mark_invoice_paid, record_attempt

MAX_ATTEMPTS = 5


def handle_payment_succeeded(event: dict) -> None:
    invoice_id = event["data"]["object"]["metadata"]["invoice_id"]
    for attempt in range(1, MAX_ATTEMPTS + 1):
        record_attempt(event["id"], attempt)
        try:
            mark_invoice_paid(invoice_id)
            return
        except Exception:
            if attempt == MAX_ATTEMPTS:
                raise
            time.sleep(2 ** attempt)
