from menu import MENU
from resources import RESOURCES

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def update_resources(action, milk, water, coffee):
    """Add or Subtract resources base on action. This function is used by the process_order() to reduce resources and
    the option Refill to add more resources."""
    water_inventory = RESOURCES["water"]
    coffee_inventory = RESOURCES["coffee"]
    milk_inventory = RESOURCES["milk"]

    if action == "reduce":
        RESOURCES["water"] = water_inventory - water
        RESOURCES["milk"] = milk_inventory - milk
        RESOURCES["coffee"] = coffee_inventory - coffee
    if action == "refill":
        RESOURCES["water"] = water_inventory + water
        RESOURCES["milk"] = milk_inventory + milk
        RESOURCES["coffee"] = coffee_inventory + coffee


def process_coins(cost):
    """Add all input coins then check if it is enough for their order. It is being used in process_order()"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (QUARTERS * quarters) + (DIMES * dimes) + (NICKLES * nickles) + (PENNIES * pennies)
    if total > coffee_cost:
        change = total - cost
        new_money = RESOURCES["money"] + cost
        RESOURCES["money"] = new_money
        return True, change
    else:
        print("Sorry that's not enough money. Money refunded")
        return False, "Exit"


def print_resources():
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money: ${RESOURCES['money']}")


def process_order(coffee, order_resources, cost):
    # ordered ingredients
    order_water_ingredient = order_resources.get("water", 0)
    order_coffee_ingredient = order_resources.get("coffee", 0)
    order_milk_ingredient = order_resources.get("milk", 0)

    # resources from the inventory
    water_inventory = RESOURCES["water"]
    coffee_inventory = RESOURCES["coffee"]
    milk_inventory = RESOURCES["milk"]

    if water_inventory < order_water_ingredient:
        print("Sorry there is not enough water")
        return False
    elif coffee_inventory < order_coffee_ingredient:
        print("Sorry there is not enough coffee")
        return False
    elif milk_inventory < order_milk_ingredient:
        print("Sorry there is not enough milk")
        return False
    else:
        # if there is enough ingredients, call coins_process() to check if the input coins is enough for their order.
        coins_process = process_coins(cost)
        coins_enough = coins_process[0]
        change = coins_process[1]
        if coins_enough:
            # if their money is enough, call the update_resources() to reduce the resource base on the ingredients used
            # by their order.
            update_resources("reduce", order_water_ingredient, order_coffee_ingredient, order_milk_ingredient)
            print(f"Here is your {change}")
            print(f"Here is your {coffee}. Enjoy!")
        return True


is_coffee_machine_on = True
while is_coffee_machine_on:
    order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if order == "off":
        is_coffee_machine_on = False
    elif order == "report":
        print_resources()
    elif order == "refill":
        # refill resources
        update_resources("refill", 1000, 1000, 500)
        print_resources()
    else:
        ordered_coffee = MENU[order]
        coffee_ingredients = ordered_coffee["ingredients"]
        coffee_cost = ordered_coffee["cost"]
        process_order = process_order(coffee=order, order_resources=coffee_ingredients, cost=coffee_cost)
