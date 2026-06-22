"""Product module for the Best Buy store project."""


class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity of the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self):
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a formatted string describing the product."""
        if self.promotion:
            return (
                f"{self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}, Promotion: {self.promotion.name}"
            )

        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0")

        if quantity > self.quantity:
            raise ValueError("Not enough stock")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity


class NonStockedProduct(Product):
    """Represents a product with unlimited stock"""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.activate()

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return quantity * self.price

    def show(self):
        if self.promotion:
            return (
                f"{self.name}, Price: {self.price}, "
                f"Quantity: Unlimited, Promotion: {self.promotion.name}"
            )

        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    """Represents a product with a maximum purchase limit"""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot buy more than {self.maximum} items of this product"
            )

        return super().buy(quantity)

    def show(self):
        if self.promotion:
            return (
                f"{self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}, Maximum: {self.maximum}, "
                f"Promotion: {self.promotion.name}"
            )

        return (
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}, Maximum: {self.maximum}"
        )
