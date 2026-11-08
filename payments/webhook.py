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


import hmac
import os


def signing_secrets() -> list[str]:
    """Current secret first, then the previous one while it is rotated out."""
    secrets = [os.environ["STRIPE_WEBHOOK_SECRET"]]
    if os.getenv("STRIPE_WEBHOOK_SECRET_PREVIOUS"):
        secrets.append(os.environ["STRIPE_WEBHOOK_SECRET_PREVIOUS"])
    return secrets


def signature_matches(payload: bytes, signature: str) -> bool:
    return any(hmac.compare_digest(hmac.new(s.encode(), payload, "sha256").hexdigest(), signature)
               for s in signing_secrets())
