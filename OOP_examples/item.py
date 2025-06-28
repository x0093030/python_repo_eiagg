class Item:
    """A class representing an item with a name, price, and quantity."""
    pay_rate = 0.8  # Class variable for discount rate
    all = []  # Class variable to store all instances
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        """        Initializes an Item instance with a name, price, and quantity.
        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item. Defaults to 0.
        """
        # Validate inputs
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"
        
        # Instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Append the instance to the class variable 'all'
        Item.all.append(self)

    @property
    def price(self):
        """Returns the price of the item."""
        return self.__price # private variable
    
    @price.setter
    def price(self, new_price: float):
        """Sets the price of the item, ensuring it is not negative."""
        assert new_price >= 0, f"Price {new_price} cannot be negative"
        self.__price = new_price
    
    def __str__(self):
        """Returns a string representation of the Item instance when using print(). aka magic method"""
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __repr__(self):
        """Returns a detailed string representation of the Item instance within a list. aka magic methdod."""
        # return f"Item({self.name!r}, {self.price!r}, {self.quantity!r})"
        return f"{self.__class__.__name__}({self.name!r}, {self.price!r}, {self.quantity!r})"

    def apply_discount(self, discount: float):
        """Applies a discount to the item's price."""
        assert 0 <= discount <= 1, "Discount must be between 0 and 1"
        self.price -= self.price * discount
        return self.price
    
    def calculate_total_price(self):
        """Calculates the total price of the item based on its quantity."""
        return self.price * self.quantity
    
    @classmethod
    def instantiate_from_json(cls):
        """Instantiates Item instances from a JSON file."""
        filename = 'items.json'
        with open(filename, 'r', encoding='utf-8') as f:
            items_data = json.load(f)
        # print(f"Instantiating items from JSON: {items_data}")
        assert isinstance(items_data, list), "JSON data must be a list of items"
        for item_data in items_data:
            name = item_data['name']
            price = item_data['price']
            quantity = item_data.get('quantity', 0)
            cls(name, price, quantity)
        return cls.all
    
    @classmethod
    def export_items_to_json(cls):
        """Exports all Item instances to a JSON file."""
        filename = 'items.json'
        items_list = [
            {
                'name': item.name,
                'price': item.price,
                'quantity': item.quantity
            }
            for item in Item.all
        ]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(items_list, f, ensure_ascii=False, indent=4)
        return items_list

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Tablet", 500, 2)
item4 = Item("Monitor", 300, 4)
item5 = Item("Keyboard", 50, 10)

# print(item1.calculate_total_price())  # Output: 500
# print(item2.calculate_total_price())  # Output: 3000
# print(Item.pay_rate)  # Output: 0.8
# print(item1.apply_discount(0.2))

# Example usage of __str__ and __repr__
# print(Item.__dict__)
# print(Item.all)  # Output: List of all Item instances
# for instance in Item.all:
#     print(instance)  # Output: Item instances with their names and prices
# print(item1)  # Output: Item(name=Phone, price=100)
