# Write a Python class Inventory with attributes like id, productName, availableQuantity and price. Add methods like addItem, updateItem, and checkItem_details.

# Use a dictionary to store the item details, where the key is the id and the value is a dictionary containing the productName, availableQuantity and price.

# Sample Data:

# {
#   "97410": {
#     "name": "Television",
#     "availableQuantity": 20,
#     "price": 1455.99
#   },
#   "97411": {
#     "name": "Radio",
#     "availableQuantity": 32,
#     "price": 654.25
#   }
# }

class Inventory:
    def __init__(self, initial_data):
        self.item_dict = initial_data

    def addItem(self):
        id = input("Enter the id: ")
        name = input("Enter the product name: ")
        availableQuantity = int(input("Enter the available quantity: "))
        price = float(input("Enter the price: "))

        # Add new item to the dictionary
        self.item_dict[id] = {
            "name": name,
            "availableQuantity": availableQuantity,
            "price": price
        }
        print(f"Item with ID {id} added successfully.")

    def updateItem(self):
        id = input("Enter the id of the item to update: ")
        if id in self.item_dict:
            name = input("Enter the new product name: ")
            availableQuantity = int(input("Enter the new available quantity: "))
            price = float(input("Enter the new price: "))
            # Update item details in the dictionary
            self.item_dict[id] = {
                "name": name,
                "availableQuantity": availableQuantity,
                "price": price
            }
            print(f"Item with ID {id} updated successfully.")

    def checkItem(self):
        id = input("Enter the id of the item to check: ")
        if id in self.item_dict:
            print(f"Item details for ID {id}:")
            print(f"Name: {self.item_dict[id]['name']}")
            print(f"Available Quantity: {self.item_dict[id]['availableQuantity']}")
            print(f"Price: {self.item_dict[id]['price']}")
        else:
            print(f"Item with ID {id} not found.")

    def __str__(self):
        result = "Inventory:\n"

        for id, details in self.item_dict.items():
            result += f"ID: {id}, Name: {details['name']}, Quantity: {details['availableQuantity']}, Price: {details['price']}\n"
        return result


# Sample initial data
initial_data = {
    "97410": {
        "name": "Television",
        "availableQuantity": 20,
        "price": 1455.99
    },
    "97411": {
        "name": "Radio",
        "availableQuantity": 32,
        "price": 654.25
    }
}

# Create Inventory instance
inventory = Inventory(initial_data)

# Print initial inventory
print(inventory)

# Add a new item
inventory.addItem()

# Print updated inventory
print(inventory)

# Update an item

inventory.updateItem()

# Print updated inventory

print(inventory)

# Check item details

inventory.checkItem()
