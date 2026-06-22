# Best Buy 2.0

A Python-based electronics store management system built with object-oriented programming principles.

## Features

- Product management
- Store inventory management
- Product promotions
- Non-stocked products
- Limited products
- Unit testing with pytest
- Command-line interface

## Product Types

### Product
Regular product with stock quantity.

### NonStockedProduct
Product with unlimited availability.

### LimitedProduct
Product with a maximum purchase limit per order.

## Promotions

### Second Half Price
Every second item is sold at 50% price.

### Third One Free
Every third item is free.

### Percent Discount
Applies a percentage discount to all purchased items.

## Project Structure

```text
main.py
products.py
store.py
promotions.py
test_produkt.py
```

## Run Application

```bash
python main.py
```

## Run Tests

```bash
python -m pytest
```

## Technologies

- Python
- Object-Oriented Programming
- Pytest
- Git & GitHub