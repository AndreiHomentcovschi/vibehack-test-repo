import csv
import datetime as dt
import io

from src.utils import format_amount


def export_invoices(invoices: list[dict], since: dt.date | None = None) -> str:
    """CSV of invoices, optionally only those issued on or after `since`."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "customer", "issued_on", "amount"])
    for invoice in invoices:
        issued_on = dt.date.fromisoformat(invoice["issued_on"])
        if since and issued_on < since:
            continue
        writer.writerow([invoice["id"], invoice["customer"], issued_on.isoformat(), format_amount(invoice["amount_cents"])])
    return buffer.getvalue()
