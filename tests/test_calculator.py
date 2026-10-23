import pytest
from app.calculator import calculate_total


def test_normal_order():
    """정상 주문 금액 계산 검증: 10,000원 x 3개 = 30,000원"""
    assert calculate_total(10000, 3) == 30000


def test_single_item():
    """단일 상품 주문 금액 계산 검증: 5,000원 x 1개 = 5,000원"""
    assert calculate_total(5000, 1) == 5000


def test_negative_price():
    """음수 가격 입력 시 ValueError 발생 검증"""
    with pytest.raises(ValueError):
        calculate_total(-1000, 2)


def test_invalid_quantity():
    """0 이하 수량 입력 시 ValueError 발생 검증"""
    with pytest.raises(ValueError):
        calculate_total(1000, 0)
