def calculate_total(price: int, quantity: int) -> int:
    """상품 단가와 수량으로 주문 총액 계산.

    Args:
        price (int): 상품 단가 (0원 이상)
        quantity (int): 주문 수량 (1개 이상)

    Returns:
        int: 총 주문 금액 (price * quantity)

    Raises:
        ValueError: price가 음수이거나 quantity가 1 미만일 때 발생
    """
    if price < 0:
        raise ValueError("상품 가격은 음수일 수 없습니다.")
    if quantity < 1:
        raise ValueError("수량은 1 이상이어야 합니다.")
    return price * quantity
