from src.auth import require_api_key
from src.export import export_invoices


def handle_export(headers: dict, invoices: list[dict]) -> tuple[int, str]:
    """HTTP handler for GET /invoices/export.csv"""
    require_api_key(headers)
    return 200, export_invoices(invoices)
