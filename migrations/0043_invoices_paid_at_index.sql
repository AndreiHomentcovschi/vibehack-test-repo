CREATE INDEX CONCURRENTLY IF NOT EXISTS invoices_paid_at_idx
    ON invoices (paid_at)
    WHERE paid_at IS NOT NULL;
