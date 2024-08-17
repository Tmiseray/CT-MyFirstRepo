from item import Item

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}

    def view_cart(self):
        for item_name, details in self.items.items():
            item, quantity = details['item'], details['quantity']
            print(f"{item_name} - ${item.price} X {quantity}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from the cart")
        else:
            print("Item not found in the cart")

    def checkout(self):
        total = sum(item['item'].price * item['quantity'] for item in self.items.values)
        print(f"Total amount: ${total}")
        self.items = {}
        print("Checkout successful.")