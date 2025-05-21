#INVENTORY MANAGEMNENT SYSTEM TO DISPLAY, UPDATE, ADD AND REMOVE ITEMS

inventory = [{"item": "apple", "quantity": 10, "price": 1000},
            {"item": "banana", "quantity": 20, "price": 500},
            {"item": "orange", "quantity": 15, "price": 1500}]

#function to display the current inventory
def display_inventory():
    print("\nCurrent Inventory:")
    print("--------------------------------------------------------------------")
    for item in inventory:
        print(f"Item: {item['item']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")   
        
    print("--------------------------------------------------------------------")    

#A function for updating inventory
def update_item():
    item_name = input("Enter the item name to update: ")
    for item in inventory:
        if item["item"] == item_name:
            quantity = int(input("Enter the new quantity: "))
            price = float(input("Enter the new price: "))
            item["quantity"] = quantity
            item["price"] = price
            print(f"Item {item_name} updated.")
            return
    print(f"Item {item_name} not found in inventory.")
    
#function to add a new item to the inventory
def add_item():
    item_name = input("Enter the new item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    inventory.append({"item": item_name, "quantity": quantity, "price": price})
    print(f"Item {item_name} added to inventory.")
    
#function to remove an item from the inventory
def remove_item():
    item_name = input("Enter the item name to remove: ")
    for item in inventory:
        if item["item"] == item_name:
            inventory.remove(item)
            print(f"Item {item_name} removed from inventory.")
            return
    print(f"Item {item_name} not found in inventory.")   
    
#Main loop to display menu and handle user input       
while True:
    print("\nInventory Management System")
    print("1. Display Inventory")
    print("2. Update Item")
    print("3. Add Item")
    print("4. Remove Item")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        display_inventory()
    elif choice == 2:
        update_item()
    elif choice == 3:
        add_item()
    elif choice == 4:
        remove_item()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")