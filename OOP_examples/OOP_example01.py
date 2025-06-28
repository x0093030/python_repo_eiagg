from item import Item  # Assuming Item class is defined in item.py
from phone import Phone  # Assuming Phone class is defined in phone.py


print(Phone.all)  # Output: List of all Phone instances
print(Item.all)  # Output: List of all Item instances

# Fix: Access the first element of Item.all, not Item itself
if Item.all:
    print(Item.all[0].name)  # Accessing the name of the first Item instance
    print(Item.all[0].price)  # Accessing the price of the first Item instance
    Item.all[0].name = "Oppo"
    # print(Item.all[0].name)  # Accessing the name of the first Item instance
    Item.all[0].price = 900
else:
    print('No Item instances found.')

print(Item.all)  # Output: List of all Item instances
