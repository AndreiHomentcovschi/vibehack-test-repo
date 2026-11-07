CREATE TABLE webhook_attempts (
    id SERIAL PRIMARY KEY,
    event_id TEXT NOT NULL,
    attempt INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
