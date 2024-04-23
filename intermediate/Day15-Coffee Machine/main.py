MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0
isOff = False


# TODO: 2- Check resource sufficient
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


# TODO-3 Process coins
def insert_coins():
    print("Please enter coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))
    price = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return price


# TODO-4 Check transaction successful
def payment_successful(money_received, cost_of_coffee):
    if money_received >= cost_of_coffee:
        change_offered = round(money_received - cost_of_coffee, 2)
        print(f"Here is ${change_offered} dollars in change.")
        global profit
        profit += cost_of_coffee
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO-5 Make coffee
def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. ☕️Enjoy!!")


while not isOff:
    # TODO: 1 - Print report of all the ingredients for coffee
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        isOff = True
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            total_payment = insert_coins()
            if payment_successful(total_payment, drink['cost']):
                make_coffee(user_input, drink['ingredients'])
