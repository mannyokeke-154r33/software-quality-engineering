import pytest

from src.token_service import issue_token


def fixed_token(length: int) -> str:
    """Deterministic stub used instead of the production random generator."""
    return "T" * length


def test_stub_makes_token_generation_deterministic():
    assert issue_token("user-42", generator=fixed_token) == "user-42:TTTTTTTTTTTT"


def test_custom_token_length_with_stub():
    assert issue_token("user-42", length=8, generator=fixed_token) == "user-42:TTTTTTTT"


def test_blank_user_id_is_rejected():
    with pytest.raises(ValueError, match="user_id is required"):
        issue_token("   ", generator=fixed_token)


def test_short_token_length_is_rejected():
    with pytest.raises(ValueError, match="at least 8"):
        issue_token("user-42", length=7, generator=fixed_token)


def test_invalid_stub_output_is_detected():
    def broken_stub(length: int) -> str:
        return "short"

    with pytest.raises(ValueError, match="unexpected token length"):
        issue_token("user-42", length=12, generator=broken_stub)
