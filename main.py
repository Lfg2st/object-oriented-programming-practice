from tabulate import tabulate
import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # Class-level list to store all instances of the Item class

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) # Add the current instance to the class-level list 'all'

    def calculate_total_price(self):
        return self.price * self.quantity # Calculate and return the total price of the item

    def apply_discount(self):
        self.price = self.price * self.pay_rate # Apply discount to the item's price

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})" # String representation of the Item instance

# Create instances of the Item class
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

def create_table(to_csv = False, path = None):
    headers = ["Name", "Price", "Quantity"]
    rows = []
    for instance in Item.all:
        print(instance) # Print each instance (Note: This is not needed for creating the table)
        rows.append([instance.name, instance.price, instance.quantity])
    if to_csv:
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
    return tabulate(rows, headers=headers, tablefmt="simple_outline")

print(create_table(to_csv = True, path = 'shop-info.csv')) # Print the table of items with their names, prices, and quantities
'''
Concepts learnt here:
1. Using tabulate:

    The tabulate library is used to create formatted tables from data, making it easy to display information in a tabular format in the terminal. It takes a list of data and generates a table with column headers and rows.
2. String representation of an object using def __repr__(self):

    The __repr__ method is a special method in Python that defines the string representation of an object. When you use print() or the str() function on an object, Python calls the __repr__ method to get a string representation of the object.
3. Instantiating a class:

    Instantiating a class means creating an object (instance) of that class. In the provided code, instances of the Item class are created using the class constructor (the __init__ method).
4. Attributes of a class:

    Attributes are variables defined within a class and represent the data associated with instances of the class. In the Item class, name, price, and quantity are attributes of each instance of the class.
5. Adding data type hints:

    Data type hints are used to specify the expected data types of function parameters and return values. In the __init__ method of the Item class, data type hints are added to the parameters name, price, and quantity to indicate their expected data types.

6. Using assert to validate inputs:

    The assert statement is used for debugging purposes to ensure that certain conditions are true. In the __init__ method, assert statements are used to validate that the price and quantity are non-negative values.
7. Class attributes vs. object attributes:

    Class attributes are shared by all instances of the class and are defined at the class level (e.g., pay_rate and all in the Item class). Object attributes are specific to each instance and are defined within the __init__ method (e.g., name, price, and quantity).
8. Printing all objects in a class using the list all which was instantiated at the level of a class:

    The all list is a class attribute in the Item class. It is used to store references to all instances of the class created so far. This allows you to access and process all instances of the class easily.
9. The self keyword:

    In Python, the self keyword is used as the first parameter in instance methods to refer to the instance (object) on which the method is called. It allows you to access and modify the object's attributes within the method.
10. Writing to a CSV:

    The code demonstrates how to export data to a CSV file using the csv module. It creates a CSV file named "items.csv" and writes the data from the Item instances to the file. The newline='' argument is used to control line endings in the CSV file.
'''