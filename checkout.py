"""Checkout total calculation with input validation."""


def checkout_total(price: int, quantity: int, coupon: int = 0) -> int:
    """상품 가격 × 수량 - 쿠폰; 잘못된 입력은 거부합니다."""
    if price < 0 or quantity < 1 or coupon < 0:
        raise ValueError("INVALID_CHECKOUT_INPUT")
    return max(0, price * quantity - coupon)
