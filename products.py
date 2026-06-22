class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self.quantity:
            raise ValueError("Not enough stock")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def __str__(self):
        output = f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

        if self.promotion:
            output += f", Promotion: {self.promotion.name}"

        return output

    def show(self):
        return str(self)

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    @property
    def quantity(self):
        return 0

    @quantity.setter
    def quantity(self, value):
        self._quantity = 0

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def __str__(self):
        output = f"{self.name}, Price: ${self.price}, Quantity: Unlimited"

        if self.promotion:
            output += f", Promotion: {self.promotion.name}"

        return output


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"You can only buy maximum {self.maximum}")

        return super().buy(quantity)

    def __str__(self):
        output = (
            f"{self.name}, Price: ${self.price}, "
            f"Quantity: {self.quantity}, Maximum: {self.maximum}"
        )

        if self.promotion:
            output += f", Promotion: {self.promotion.name}"

        return output
