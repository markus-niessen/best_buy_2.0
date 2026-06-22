"""Command line interface for the Best Buy store project."""

import products
import store
import promotions


def start(store_obj):
    """Start the store menu interface."""
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            for index, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{index}. {product}")
            print("------")

        elif choice == "2":
            print(f"Total of {store_obj.get_total_quantity()} items in store")

        elif choice == "3":
            shopping_list = []
            all_products = store_obj.get_all_products()

            print("------")
            for index, product in enumerate(all_products, start=1):
                print(f"{index}. {product}")
            print("------")
            print("When you want to finish order, enter empty text.")

            while True:
                product_number = input("Which product # do you want? ")

                if product_number == "":
                    break

                amount = input("What amount do you want? ")

                try:
                    product_number = int(product_number)
                    amount = int(amount)

                    product = all_products[product_number - 1]
                    shopping_list.append((product, amount))

                    print("Product added to list!\n")

                except (ValueError, IndexError):
                    print("Error adding product!\n")

            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total_price}")
                except ValueError as error:
                    print("********")
                    print(f"Order failed: {error}")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def main():
    """Create the store and start the program."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct(
            "Shipping",
            price=10,
            quantity=250,
            maximum=1
        )
    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()