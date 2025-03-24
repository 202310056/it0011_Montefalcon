class Item:
    def __init__(self, id, name, itemDesc, price):
        self.id = id
        self.name = name
        self.itemDesc = itemDesc
        self.price = price

    def __str__(self):
        return f"Item ID: {self.id} \nName: {self.name} \nDescription: {self.itemDesc} \nPrice: ${self.price}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, id, name, itemDesc, price):
        try:
            if not id or not name or not itemDesc or not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Invalid item data! Please check and try again.")
            if id in self.items:
                raise KeyError(f"Item with ID {id} already exists.")
            new_item = Item(id, name, itemDesc, price)
            self.items[id] = new_item
            print(f"Item with ID {id} created successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError as ke:
            print(f"Error: {ke}")

    def read_item(self, id):
        try:
            if id not in self.items:
                raise KeyError(f"Item with ID {id} not found.")
            print(self.items[id])
        except KeyError as ke:
            print(f"Error: {ke}")

    def update_item(self, id, name=None, itemDesc=None, price=None):
        try:
            if id not in self.items:
                raise KeyError(f"Item with ID {id} not found.")
            item = self.items[id]
            if name:
                item.name = name
            if itemDesc:
                item.itemDesc = itemDesc
            if price is not None:
                if price <= 0 or not isinstance(price, (int, float)):
                    raise ValueError("Price must be a positive number.")
                item.price = price
            print(f"Item with ID {id} updated successfully.")
        except KeyError as ke:
            print(f"Error: {ke}")
        except ValueError as ve:
            print(f"Error: {ve}")

    def delete_item(self, id):
        try:
            if id not in self.items:
                raise KeyError(f"Item with ID {id} not found.")
            del self.items[id]
            print(f"Item with ID {id} deleted successfully.")
        except KeyError as ke:
            print(f"Error: {ke}")

    def list_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)


def main():
    manager = ItemManager()

    while True:
        print("\n------------------------")
        print("| Item Management Menu |")
        print("------------------------")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List All Items")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                id = input("Enter Item ID: ")
                name = input("Enter Item Name: ")
                itemDesc = input("Enter Item Description: ")
                price = float(input("Enter Item Price: "))
                manager.create_item(id, name, itemDesc, price)
            except ValueError:
                print("Error: Price must be a number.")
        elif choice == "2":
            id = input("Enter Item ID to view: ")
            manager.read_item(id)
        elif choice == "3":
            id = input("Enter Item ID to update: ")
            name = input("Enter new Item Name: ")
            itemDesc = input("Enter new Item Description: ")
            price_input = input("Enter new Item Price: ")
            price = float(price_input) if price_input else None
            manager.update_item(id, name, itemDesc, price)
        elif choice == "4":
            id = input("Enter Item ID to delete: ")
            manager.delete_item(id)
        elif choice == "5":
            manager.list_items()
        elif choice == "6":
            print("Thank you for using the application! :)")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()