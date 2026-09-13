"""Checkout behavior tests."""

import pytest

from checkout import checkout_total


def test_normal_coupon():
    assert checkout_total(12000, 2, 3000) == 21000


def test_coupon_cannot_make_total_negative():
    assert checkout_total(1000, 1, 5000) == 0


def test_exact_coupon_total_is_valid():
    assert checkout_total(1000, 2, 2000) == 0


def test_coupon_defaults_to_zero():
    assert checkout_total(2500, 3) == 7500


def test_coupon_below_total_keeps_positive_payment():
    assert checkout_total(1000, 3, 500) == 2500


def test_zero_price_is_valid():
    assert checkout_total(0, 1, 0) == 0


def test_minimum_quantity_is_valid():
    assert checkout_total(1000, 1, 0) == 1000


@pytest.mark.parametrize(
    "args",
    [(-1, 1, 0), (1000, 0, 0), (1000, 1, -1), (1000, -1, 0)],
)
def test_invalid_input_is_rejected(args):
    with pytest.raises(ValueError):
        checkout_total(*args)


def test_invalid_input_has_stable_error_code():
    with pytest.raises(ValueError, match="INVALID_CHECKOUT_INPUT"):
        checkout_total(1000, -1, 0)
