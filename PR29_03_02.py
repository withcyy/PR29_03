class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, item_name, item_price, quantity=1):
        if item_name in self.__items:
            self.__items[item_name] += quantity
        else:
            self.__items[item_name] = quantity

    def calculate_total(self):
        total = 0
        for item_name, quantity in self.__items.items():
            total += quantity * item_price[item_name]
        return total

item_price = {
    "apple": 2,
    "banana": 3,
    "orange": 4
}

cart = ShoppingCart()

cart.add_item("apple", item_price["apple"], 2)
cart.add_item("banana", item_price["banana"])
cart.add_item("orange", item_price["orange"], 3)

total_cost = cart.calculate_total()
print("Загальна вартість покупок:", total_cost)