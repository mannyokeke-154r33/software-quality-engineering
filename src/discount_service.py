"""Business rules used to demonstrate requirements-based test design."""

from decimal import Decimal, ROUND_HALF_UP


MONEY = Decimal("0.01")
MAX_DISCOUNT = Decimal("250.00")


def _money(value: Decimal) -> Decimal:
    return value.quantize(MONEY, rounding=ROUND_HALF_UP)


def discount_rate(total: Decimal) -> Decimal:
    """Return the discount rate associated with a purchase total."""
    if total < Decimal("0"):
        raise ValueError("purchase total cannot be negative")
    if total < Decimal("50"):
        return Decimal("0")
    if total < Decimal("100"):
        return Decimal("0.05")
    return Decimal("0.10")


def calculate_discount(total: Decimal) -> Decimal:
    """Calculate a rounded discount while enforcing the discount cap."""
    rate = discount_rate(total)
    return min(_money(total * rate), MAX_DISCOUNT)


def final_total(total: Decimal) -> Decimal:
    """Return the amount due after the applicable discount."""
    return _money(total - calculate_discount(total))
