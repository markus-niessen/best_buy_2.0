"""Promotion module for the Best Buy store project."""

from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    """Applies a percentage discount."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * self.percent / 100
        return total_price - discount


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2

        return (
                (full_price_items * product.price)
                + (half_price_items * product.price * 0.5)
        )


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * product.price
