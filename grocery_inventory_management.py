inventory = {}
def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory[name] = {'quantity': quantity, 'price': price}
    print(f"{name} added to inventory.\n")
def update_quantity():
    """Update the quantity of an existing item."""
    name = input("Enter item name to update quantity: ")
    if name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[name]['quantity'] = new_quantity
        print(f"Quantity of {name} updated to {new_quantity}.\n")
    else:
        print(f"{name} is not in the inventory.\n")
def view_inventory():
    """View the current inventory."""
    print("Current Inventory:")
    for item, details in inventory.items():
        print(f"{item}: Quantity - {details['quantity']}, Price - ${details['price']:.2f}")
    print()
def remove_item():
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.\n")
    else:
        print(f"{name} is not in the inventory.\n")
while True:
    print("Menu:")
    print("1. Add new item")
    print("2. Update item quantity")
    print("3. View inventory")
    print("4. Remove item")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_item()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.\n")
