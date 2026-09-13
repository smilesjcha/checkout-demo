"""Checkout behavior tests."""

import pytest

from checkout import checkout_total


def test_normal_coupon():
    assert checkout_total(12000, 2, 3000) == 21000


def test_coupon_cannot_make_total_negative():
    assert checkout_total(1000, 1, 5000) == 0


def test_exact_coupon_total_is_valid():
    assert checkout_total(1000, 2, 2000) == 0


@pytest.mark.parametrize(
    "args",
    [(-1, 1, 0), (1000, 0, 0), (1000, 1, -1), (1000, -1, 0)],
)
def test_invalid_input_is_rejected(args):
    with pytest.raises(ValueError):
        checkout_total(*args)
