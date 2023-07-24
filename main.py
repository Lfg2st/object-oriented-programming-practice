from tabulate import tabulate
import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []  # Class-level list to store all instances of the Item class

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)  # Add the current instance to the class-level list 'all'

    def calculate_total_price(self):
        return (
            self.price * self.quantity
        )  # Calculate and return the total price of the item

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # Apply discount to the item's price

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"  # String representation of the Item instance


# Create instances of the Item class
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


def create_table(to_csv=False, path=None):
    headers = ["Name", "Price", "Quantity"]
    rows = []
    for instance in Item.all:
        print(
            instance
        )  # Print each instance (Note: This is not needed for creating the table)
        rows.append([instance.name, instance.price, instance.quantity])
    if to_csv:
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
    return tabulate(rows, headers=headers, tablefmt="simple_outline")


print(
    create_table(to_csv=True, path="shop-info.csv")
)  # Print the table of items with their names, prices, and quantities
