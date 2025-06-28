from item import Item  # Assuming Item class is defined in item.py


class Phone(Item):
    """A class representing a phone item, inheriting from Item and using super() functionality."""
    all = []  # Class variable to store all Phone instances, don't needed due to super() functionality

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phone: int = 0):
        super().__init__(name, price, quantity)
        # self.type = 'Phone'
        assert broken_phone >= 0, f"Broken phones {broken_phone} cannot be negative"
        self.broken_phone = broken_phone
        Phone.all.append(self)  # don't needed due to super() functionality


# Export all items to a JSON file and print the JSON content
# items_json = Item.export_items_to_json()
# print(json.dumps(items_json, ensure_ascii=False, indent=4))

# Once DB is created, instantiate from JSON file 
# print(Item.instantiate_from_json())

# Example of Inheritance + super() + class name
phone1 = Phone("iPhone", 999, 10, 2)
phone2 = Phone("Samsung Galaxy", 899, 5, 1)
print(phone1.calculate_total_price())
