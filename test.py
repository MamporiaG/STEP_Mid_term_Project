from restaurant import Restaurant, MenuItem, Wines
import pandas as pd

def main():

    # Instances

    cheese_board = MenuItem("cheese board", 12, "appetizer")
    pizza_margarita = MenuItem("pizza margarita", 20, "Pizza")
    pasta_carbonara = MenuItem("pasta carbonara", 25, "Pasta")
    ribeye_steak = MenuItem("ribeye steak", 55, "main dish")
    cheesecake = MenuItem("cheesecake", 15, "dessert", is_available=False)
    saperavi = Wines("saperavi", 35, "Red", "2021", "Dry", "Georgia")
    tsolikouri = Wines("tsolikouri", 27, "White", "2024", "Semi dry", "Georgia")
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

    # Describe item

    saperavi_description = saperavi.describe_item()
    print(saperavi_description)

    # Print menu

    my_restaurant.print_whole_menu()

    # Print by category

    my_restaurant.print_by_category("main dish")

    # Remove menu item

    my_restaurant.remove_menu_item(pasta_carbonara)

    # Update price of ribeye steaak

    my_restaurant.update_price("ribeye steak", 70)

    # Calculate order price

    order_price = my_restaurant.calculate_order(
        {
            "whisky": 5,
            "saperavi": 2,
            "ribeye steak": 2,
            "pizza margarita": 1,
            "khachapuri": 1,
        }
    )

    print(f"\n Total price of the order is: ${order_price}")

    # Extract and read csv file
    my_restaurant.extract_to_csv()
    df = pd.read_csv("menu.csv")
    print(df)

if __name__ == "__main__":
    main()

