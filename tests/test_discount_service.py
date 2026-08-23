from decimal import Decimal

import pytest

from src.discount_service import calculate_discount, discount_rate, final_total


@pytest.mark.parametrize(
    ("total", "expected_rate"),
    [
        ("0.00", "0"),
        ("25.00", "0"),
        ("49.99", "0"),
        ("50.00", "0.05"),
        ("75.00", "0.05"),
        ("99.99", "0.05"),
        ("100.00", "0.10"),
        ("250.00", "0.10"),
    ],
)
def test_equivalence_partitions(total, expected_rate):
    assert discount_rate(Decimal(total)) == Decimal(expected_rate)


@pytest.mark.parametrize(
    ("total", "expected_rate"),
    [
        ("49.99", "0"),
        ("50.00", "0.05"),
        ("50.01", "0.05"),
        ("99.99", "0.05"),
        ("100.00", "0.10"),
        ("100.01", "0.10"),
    ],
)
def test_boundary_values(total, expected_rate):
    assert discount_rate(Decimal(total)) == Decimal(expected_rate)


def test_negative_total_is_rejected():
    with pytest.raises(ValueError, match="cannot be negative"):
        discount_rate(Decimal("-0.01"))


def test_discount_is_rounded_to_currency_precision():
    assert calculate_discount(Decimal("50.01")) == Decimal("2.50")


def test_discount_cap_is_enforced():
    assert calculate_discount(Decimal("5000.00")) == Decimal("250.00")


def test_final_total_applies_discount():
    assert final_total(Decimal("100.00")) == Decimal("90.00")


def test_regression_exact_100_receives_ten_percent_rate():
    """Protect the exact $100 boundary from a past >= versus > defect."""
    assert discount_rate(Decimal("100.00")) == Decimal("0.10")
