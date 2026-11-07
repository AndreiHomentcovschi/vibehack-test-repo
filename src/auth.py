import hmac
import os


class Unauthorized(Exception):
    pass


def require_api_key(headers: dict) -> None:
    """Rejects requests without the X-Api-Key header matching EXPORT_API_KEY."""
    expected = os.environ.get("EXPORT_API_KEY")
    if not expected:
        raise Unauthorized("export API key is not configured")
    if not hmac.compare_digest(headers.get("X-Api-Key", ""), expected):
        raise Unauthorized("invalid API key")
