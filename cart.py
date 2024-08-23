# #how to use dictionary as mam
# class cart:
#     def __init__(self):
#         self.product_name=[]
#         self.quantity=[]
#         self.costp=100
#         self.Total_cost=0
#
#     def Items_Available(self):
#         list_items=['papaya','guava','orange','mango','apple']
#         print("The items available are")
#         for i in list_items:
#             print(i)
#     def add_item(self):
#         product_name=input("enter the Item you want")
#         quantity=int(input("enter the quantity"))
#         self.product_name.append(product_name)
#         self.cost=
#         self.quantity.append(quantity)
#
#
#     def remove_item(self):
#         product_name = input("enter the Item you want")
#         quantity = int(input("enter the quantity"))
#         self.product_name.remove(product_name)
#         self.quantity.remove(quantity)
#     def Bill(self):
#         print(self.product_name)
#         print(self.quantity)
#
# c1=cart()
# c1.Items_Available()
# c1.add_item()
# c1.Bill()
#
#
class ShoppingCart:
    def __init__(self):
        self.cart = {}  # Dictionary to hold item names as keys and a tuple (price, quantity) as values
        self.available_items = {  # Predefined available items with prices
            "Apple": 0.99,
            "Banana": 0.5,
            "Orange": 0.75,
            "Milk": 2.0,
            "Bread": 1.5
        }

    def show_available_items(self):
        """Display the available items and their prices."""
        print("Available items:")
        for item_name, price in self.available_items.items():#to get both key and value we use items
            print(f"{item_name}: ${price}")

    def add_item(self, item_name, quantity=1):
        """Add an item to the cart with the given price and quantity."""
        if item_name in self.available_items:
            price = self.available_items[item_name]
            if item_name in self.cart:
                self.cart[item_name] = (price, self.cart[item_name][1] + quantity)
            else:
                self.cart[item_name] = (price, quantity)
            print(f"Added {quantity} x {item_name}(s) to the cart.")
        else:
            print(f"{item_name} is not available in the store.")

    def remove_item(self, item_name, quantity=1):
        """Remove a certain quantity of an item from the cart."""
        if item_name in self.cart:
            current_quantity = self.cart[item_name][1]#1 bcoz 0 is price and 1 is quantity
            if quantity >= current_quantity:
                del self.cart[item_name]
                print(f"Removed all {item_name}(s) from the cart.")
            else:
                self.cart[item_name] = (self.cart[item_name][0], current_quantity - quantity)
                print(f"Removed {quantity} x {item_name}(s) from the cart.")
        else:
            print(f"{item_name} is not in the cart.")

    def view_cart(self):
        """Display all items in the cart with their prices and quantities."""
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item_name, (price, quantity) in self.cart.items():
                print(f"{item_name}: ${price} each, Quantity: {quantity}")

    def total_price(self):
        """Calculate the total price of all items in the cart."""
        total = sum(price * quantity for price, quantity in self.cart.values())
        print(f"The total price of all items in the cart is: ${total:.2f}")
        return total


# Interactive menu for user input
def main():
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. Show available items")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Total price")
        print("6. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == "1":
            cart.show_available_items()

        elif choice == "2":
            cart.show_available_items()
            item_name = input("Enter the item name to add: ")
            quantity = int(input("Enter the quantity: "))
            cart.add_item(item_name, quantity)

        elif choice == "3":
            item_name = input("Enter the item name to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            cart.remove_item(item_name, quantity)

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.total_price()

        elif choice == "6":
            print("Exiting the program. Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":#what is this main
    main()
