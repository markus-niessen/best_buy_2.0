import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product. is_active() is True

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_buy_product_changes_quantity_and_returns_total_price():
    product = Product("MacBook Air M2", price=1450, quantity=100)

    result = product.buy(2)

    assert product.quantity == 98
    assert result == 2900

def test_product_becomes_inactive_when_quantity_reaches_zero():
    product = Product("MacBook Air M2", price=1450,
                       quantity=1)
    product.buy(1)

    assert product.quantity == 0
    assert product.is_active() is False

def test_buy_more_than_available_quantity():
    product =Product("MacBook Air M2", price=1450, quantity=5)

    with pytest.raises(ValueError):
        product.buy(10)