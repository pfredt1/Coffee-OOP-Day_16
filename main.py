from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
# mi = MenuItem()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on == True:
    order = input(f"What would you like to order? {menu.get_items()} ")
    if order == "off":
        is_on = False
    elif order == "reports":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(order)
        (coffee_maker.is_resource_sufficient(menu_item))
        money_machine.make_payment(menu_item.cost)
        coffee_maker.make_coffee(menu_item)


