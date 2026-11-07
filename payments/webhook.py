from payments.db import mark_invoice_paid


def handle_payment_succeeded(event: dict) -> None:
    invoice_id = event["data"]["object"]["metadata"]["invoice_id"]
    mark_invoice_paid(invoice_id)
