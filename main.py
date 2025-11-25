import pandas as pd


class MenuItem:
    def __init__(self, name, price, category, is_available=True):
        self.name = name.title()
        self.price = price
        self.category = category.title()
        self.is_available = is_available


class Wines(MenuItem):
    def __init__(self, name, price, category="wines", is_available=True):
        super().__init__(name, price, category, is_available)


class Restaurant:
    def __init__(self, name):
        self.name = name.title()
        self.menu = []

    def add_menu_item(self, menu_item):
        self.menu.append(menu_item)
        print(f"{menu_item.name} has been added to the menu")

    def remove_menu_item(self, menu_item):
        for item in self.menu:
            if item.name == menu_item.name:
                self.menu.remove(item)
                print(f"\nThe {menu_item.name} has been removed from the menu")
                return
        print(f"\n{menu_item.name} hasn't been found in the menu")

    def update_price(self, item_name, new_price):
        if new_price < 0:
            print("Enter a correct price")
            return

        for item in self.menu:
            if item.name.lower() == item_name.lower():
                item.price = new_price
                print(
                    f"\n{item_name.title()} price has been updated to ${new_price:.2f}"
                )
                return
        print(f"{item_name} isn't in the menu")

    def print_whole_menu(self):
        print(f"\nRestaurant {self.name} Menu:\n")
        for item in self.menu:
            if item.is_available:
                print(f" - {item.name}: ${item.price:.2f}")

    def print_by_category(self, category):
        print(f"\n{category.capitalize()} Menu:")
        available_items = [
            item
            for item in self.menu
            if item.category.lower() == category.lower() and item.is_available
        ]
        if available_items:
            for item in available_items:
                print(f" - {item.name}: ${item.price:.2f}")
        else:
            print(f"No items avaialble for this category")

    def calculate_order(self, ordered_items):
        total_cost = 0
        vat = 0.18
        for k, v in ordered_items.items():
            available_order = [
                item for item in self.menu if k.lower() == item.name.lower()
            ]
            if available_order:
                item = available_order[0]
                if item.is_available:
                    print(f"Item: {k.title()}, quantity: {v}")
                    total_cost += v * item.price
                else:
                    print(f"{k.title()} isn't available at the moment")
            else:
                print(f"{k.title()} isn't on the menu")
        print(f"Total cost of the order is ${total_cost * (1 + vat):.2f}")

    def extract_to_csv(self, filename="menu.csv"):
        data = []
        for item in self.menu:
            data.append(
                {
                    "Name": item.name,
                    "Price": item.price,
                    "Category": item.category,
                    "Availability": item.is_available,
                }
            )
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"{filename} has been created\n")


# Instances

cheese_board = MenuItem("cheese board", 12, "appetizer")
pizza_margarita = MenuItem("pizza margarita", 20, "Pizza")
pasta_carbonara = MenuItem("pasta carbonara", 25, "Pasta")
ribeye_steak = MenuItem("ribeye steak", 55, "main dish")
cheesecake = MenuItem("cheesecake", 15, "dessert", is_available=False)
saperavi = Wines("saperavi", 35)
tsolikouri = Wines("tsolikouri", 27)
whisky = MenuItem("whisky", 27, "alcoholic beverage", is_available=False)

my_restaurant = Restaurant("Tbilisi")

print("Adding items to the menu:\n")

my_restaurant.add_menu_item(cheese_board)
my_restaurant.add_menu_item(pizza_margarita)
my_restaurant.add_menu_item(pasta_carbonara)
my_restaurant.add_menu_item(ribeye_steak)
my_restaurant.add_menu_item(cheesecake)
my_restaurant.add_menu_item(saperavi)
my_restaurant.add_menu_item(tsolikouri)
my_restaurant.add_menu_item(whisky)


# Print menu

my_restaurant.print_whole_menu()

# Print by category

my_restaurant.print_by_category("main dish")

# Remove menu item

my_restaurant.remove_menu_item(pasta_carbonara)

# Update price of ribeye steaak

my_restaurant.update_price("ribeye steak", 70)

# Calculate order price

my_restaurant.calculate_order(
    {
        "whisky": 5,
        "saperavi": 2,
        "ribeye steak": 2,
        "pizza margarita": 1,
        "khachapuri": 1,
    }
)

my_restaurant.extract_to_csv()
df = pd.read_csv("menu.csv")
print(df)
