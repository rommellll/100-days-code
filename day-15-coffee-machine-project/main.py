from menu import MENU
from resources import RESOURCES


def update_resources(action, milk, water, coffee):
    """Add or Subtract resources base on action.
    It requires input of action (reduce or refill) and the number of resources for coffee, milk and water to be added or
    subtracted.
    This function is used by the process_order() to reduce resources and the option Refill to add more resources."""
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


def update_money(action,amount):
    if action == "add":
        new_money = RESOURCES["money"] + amount
        RESOURCES["money"] = new_money
    elif action == "subtract":
        new_money = RESOURCES["money"] - amount
        RESOURCES["money"] = new_money


def process_coins(cost):
    """Add all input coins then check if it is enough for their order. It is being used in process_order()"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if total >= coffee_cost:
        change = round(total - cost, 2)
        return True, change
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, total


def print_resources():
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money: ${RESOURCES['money']}")


def check_resources(order_resources):
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
        return True


def process_order(coffee, order_resources, change,cost):
    order_water_ingredient = order_resources.get("water", 0)
    order_coffee_ingredient = order_resources.get("coffee", 0)
    order_milk_ingredient = order_resources.get("milk", 0)

    # if their money is enough, call the update_resources() to reduce the resource base on the ingredients used
    # by their order.
    update_resources("reduce", order_water_ingredient, order_coffee_ingredient, order_milk_ingredient)
    update_money("add", cost)
    print(f"Here is your change ${change}")
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
    elif (order == "espresso") or (order == "latte") or (order == "cappuccino"):
        ordered_coffee = MENU[order]
        coffee_ingredients = ordered_coffee["ingredients"]
        coffee_cost = ordered_coffee["cost"]
        enough_resources = check_resources(order_resources=coffee_ingredients)
        if enough_resources:
            transaction = process_coins(coffee_cost)
            transaction_successful = transaction[0]
            order_change = transaction[1]
            if transaction_successful:
                task = process_order(order, coffee_ingredients, order_change, coffee_cost)
    else:
        print("Sorry! We don't have that kind of coffee.")
