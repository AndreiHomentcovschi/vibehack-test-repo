import csv
import io

from src.utils import format_amount


def export_invoices(invoices: list[dict]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "customer", "amount"])
    for invoice in invoices:
        writer.writerow([invoice["id"], invoice["customer"], format_amount(invoice["amount_cents"])])
    return buffer.getvalue()
