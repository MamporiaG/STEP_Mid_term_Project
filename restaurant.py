import pandas as pd
VAT = 0.18

class MenuItem:
    def __init__(self, name, price, category, is_available=True):
        self.name = name.title()
        self.price = price
        self.category = category.title()
        self.is_available = is_available
    
    def describe_item(self):
        return f"{self.name}: ${self.price}"


class Wines(MenuItem):
    def __init__(self, name, price, colour, vintage, type, country, is_available=True):
        super().__init__(name, price, category="Wines", is_available=is_available)
        self.colour = colour.capitalize()
        self.vintage = vintage
        self.type = type.capitalize()
        self.country = country.title()

    def describe_item(self):
        return f"\n - Name: {self.name}\n - Colour:{self.colour}\n - Type: {self.type}\n - Country: {self.country}\n - Vintage: {self.vintage}\n - Price: ${self.price}"



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
        for k, v in ordered_items.items():

            try:
                v = int(v)
                if v < 0:
                    print("Quantity of items cannot be negative.")
                    continue
            except (ValueError, TypeError):
                print("Invalid quantity. Please, enter a correct order.")
                continue

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
            grand_total = total_cost * (1 + VAT)
        return grand_total

    def extract_to_csv(self, filename="menu.csv"):
        data = []
        for item in self.menu:
            rows = {
                    "Name": item.name,
                    "Price": item.price,
                    "Category": item.category,
                    "Availability": item.is_available,
                    "Colour": None,
                    "Vintage": None,
                    "Type": None,
                    "Country": None
                }
            if item.category == "Wines":
                rows["Colour"] = item.colour
                rows["Vintage"] = item.vintage
                rows["Type"] = item.type
                rows["Country"] = item.country
            
            data.append(rows)
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"{filename} has been created\n")
