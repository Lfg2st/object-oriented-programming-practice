import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    # instantiating from csv using a class method (a method which is not bound to a particular class but the class itself - this allows us to do class level modifications and capturing attributes)
    @classmethod
    def instantiate_from_csv(cls):
        datalist = []
        with open('shop-info.csv', 'r') as f:
            csv_reader = csv.DictReader(f)
            items = list(csv_reader)
        for item in items:
            Item(
                name = item['name'],
                price = float(item['price']),
                quantity = float(item['quantity'])
            )

    @staticmethod #class reference is not the first argument, one can use it just like any another function
    def is_integer(num):
        if num % 1 == 0:
            True
        else:
            False
Item.instantiate_from_csv()
print(Item.all)