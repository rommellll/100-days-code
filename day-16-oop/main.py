from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
pos = MoneyMachine()


coffee_machine_on = True
while coffee_machine_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        coffee_machine_on = False
        print("Going to maintenance mode.")
    elif order == "report":
        coffee_maker.report()
        pos.report()
    elif (order == "latte") or (order == "espresso") or (order == "cappuccino"):
        item = menu.find_drink(order)
        cost = item.cost
        resource_sufficient = coffee_maker.is_resource_sufficient(item)
        if resource_sufficient:
            payment_enough = pos.make_payment(cost)
            if payment_enough:
                coffee_maker.make_coffee(item)
    else:
        print("Sorry we don't have that item.")