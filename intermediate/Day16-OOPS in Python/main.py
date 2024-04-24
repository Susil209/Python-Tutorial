# from turtle import Turtle, Screen
#
# # create a turtle object
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# my_turtle.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

# Prettytable
# from prettytable import PrettyTable
#
# table = PrettyTable()
# # Column by column
# table.add_column("Pokemon name", ["Pikachu", "Sqartle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.header = True
# table.align = 'l'
# print(table)


# Coffee-machine

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOff = False
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not isOff:
    user_input = input(f"What would you like? ({menu.get_items()}):")
    if user_input == "off":
        isOff = True
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)