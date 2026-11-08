# Invoice Service

Small service that exports invoices and receives payment webhooks from Stripe.

## Modules
- `src/utils.py` — formatting helpers
- `src/export.py` — invoice CSV export
- `payments/webhook.py` — Stripe webhook handler with retries
- `payments/db.py` — payment state and webhook attempt log
- `migrations/` — SQL migrations, applied in order

## Export columns
| column | type |
|---|---|
| number | INV-YYYY-NNNNN |
| issued_at | ISO date |
| amount | cents, integer |
| currency | ISO 4217 |
