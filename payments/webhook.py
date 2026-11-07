import hashlib
import hmac
import os
import time

from payments.db import mark_invoice_paid, record_attempt

MAX_ATTEMPTS = 5
TOLERANCE_SECONDS = 300


class InvalidSignature(Exception):
    pass


def verify_signature(payload: bytes, header: str, secret: str | None = None) -> None:
    """Checks a Stripe-Signature header (t=timestamp,v1=signature) against the endpoint secret."""
    secret = secret or os.environ["STRIPE_WEBHOOK_SECRET"]
    parts = dict(item.split("=", 1) for item in header.split(","))
    timestamp = int(parts["t"])
    if abs(time.time() - timestamp) > TOLERANCE_SECONDS:
        raise InvalidSignature("timestamp outside tolerance")
    expected = hmac.new(secret.encode(), f"{timestamp}.".encode() + payload, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, parts.get("v1", "")):
        raise InvalidSignature("signature mismatch")


def handle_payment_succeeded(event: dict, payload: bytes, signature_header: str) -> None:
    verify_signature(payload, signature_header)
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
