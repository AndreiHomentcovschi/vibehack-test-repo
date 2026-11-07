import datetime as dt

from src.export import export_invoices

INVOICES = [
    {"id": "inv_1", "customer": "Acme", "issued_on": "2026-10-01", "amount_cents": 1250},
    {"id": "inv_2", "customer": "Globex", "issued_on": "2026-11-05", "amount_cents": 990},
]


def test_exports_all_by_default():
    assert export_invoices(INVOICES).count("\n") == 3


def test_filters_by_date():
    out = export_invoices(INVOICES, since=dt.date(2026, 11, 1))
    assert "inv_2" in out and "inv_1" not in out
