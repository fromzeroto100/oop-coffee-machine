from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True

while is_on:
    choice = input("What would you like? latte/espresso/cappuccino: ")
