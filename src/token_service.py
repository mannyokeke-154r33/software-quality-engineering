"""Example service with an injectable dependency for deterministic testing."""

import secrets
from collections.abc import Callable


TokenGenerator = Callable[[int], str]


def random_token(length: int) -> str:
    return secrets.token_hex(length)[:length]


def issue_token(user_id: str, length: int = 12, generator: TokenGenerator = random_token) -> str:
    """Issue a user token using a replaceable token generator."""
    if not user_id.strip():
        raise ValueError("user_id is required")
    if length < 8:
        raise ValueError("token length must be at least 8")

    token = generator(length)
    if len(token) != length:
        raise ValueError("generator returned an unexpected token length")

    return f"{user_id}:{token}"
