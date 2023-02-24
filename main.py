# IMPORTS
import data


def take_coins():
    total_money = 0
    quarters = int(input("How many quarters? "))
    total_money += quarters * .25
    dimes = int(input("How many dimes? "))
    total_money += dimes * .10
    nickles = int(input("How many nickles? "))
    total_money += nickles * .05
    pennies = int(input("How many pennies? "))
    total_money += pennies * .01

    return total_money


def task(job):
    drink_successfully_brewed = True

    if job == "off":
        return False
    elif job == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${data.resources['money']}")
    elif job == "espresso":
        # not enough water
        if data.MENU['espresso']['ingredients']['water'] > data.resources['water']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough water for your drink.")
        # not enough coffee
        elif job == "espresso" and data.MENU['espresso']['ingredients']['coffee'] > data.resources['coffee']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough coffee for your drink.")
        # espresso water
        if data.resources['water'] >= data.MENU['espresso']['ingredients']['water']:
            data.resources['water'] -= data.MENU['espresso']['ingredients']['water']
        # espresso coffee
        if data.resources['coffee'] >= data.MENU['espresso']['ingredients']['coffee']:
            data.resources['coffee'] -= data.MENU['espresso']['ingredients']['coffee']
        if drink_successfully_brewed:
            money_paid = take_coins()
            if data.MENU['espresso']['cost'] > money_paid:
                print("Sorry that's not enough money.")
            else:
                money_paid -= data.MENU['espresso']['cost']
                data.resources['money'] += data.MENU['latte']['cost']
                print(f"You paid too much. ${money_paid} is refunded.")
                print()
                print("Here's your espresso! Thanks for your business today!")
    elif job == 'latte':
        # not enough water
        if data.MENU['latte']['ingredients']['water'] > data.resources['water']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough water for your drink.")
        # not enough milk
        elif data.MENU['latte']['ingredients']['milk'] > data.resources['milk']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough milk for your drink.")
        # not enough coffee
        elif data.MENU['latte']['ingredients']['coffee'] > data.resources['coffee']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough coffee for your drink.")
        # latte water
        if data.resources['water'] >= data.MENU['latte']['ingredients']['water']:
            data.resources['water'] -= data.MENU['latte']['ingredients']['water']
        # latte milk
        if data.resources['milk'] >= data.MENU['latte']['ingredients']['milk']:
            data.resources['milk'] -= data.MENU['latte']['ingredients']['milk']
        # latte coffee
        if data.resources['coffee'] >= data.MENU['latte']['ingredients']['coffee']:
            data.resources['coffee'] -= data.MENU['latte']['ingredients']['coffee']
        if drink_successfully_brewed:
            money_paid = take_coins()
            if data.MENU['espresso']['cost'] > money_paid:
                print("Sorry that's not enough money.")
            else:
                money_paid -= data.MENU['espresso']['cost']
                data.resources['money'] += data.MENU['latte']['cost']
                print(f"You paid too much. ${money_paid} is refunded.")
                print()
                print("Here's your espresso! Thanks for your business today!")
    elif job == 'cappuccino':
        # not enough water
        if data.MENU['cappuccino']['ingredients']['water'] > data.resources['water']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough water for your drink.")
        # not enough milk
        elif data.MENU['cappuccino']['ingredients']['milk'] > data.resources['milk']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough milk for your drink.")
        # not enough coffee
        elif data.MENU['cappuccino']['ingredients']['coffee'] > data.resources['coffee']:
            drink_successfully_brewed = False
            print("Sorry. There's not enough coffee for your drink.")
        # cappuccino water
        if data.resources['water'] >= data.MENU['cappuccino']['ingredients']['water']:
            data.resources['water'] -= data.MENU['cappuccino']['ingredients']['water']
        # cappuccino milk
        if data.resources['milk'] >= data.MENU['cappuccino']['ingredients']['milk']:
            data.resources['milk'] -= data.MENU['cappuccino']['ingredients']['milk']
        # cappuccino coffee
        if data.resources['coffee'] >= data.MENU['cappuccino']['ingredients']['coffee']:
            data.resources['coffee'] -= data.MENU['cappuccino']['ingredients']['coffee']
        if drink_successfully_brewed:
            money_paid = take_coins()
            if data.MENU['espresso']['cost'] > money_paid:
                print("Sorry that's not enough money.")
            else:
                money_paid -= data.MENU['espresso']['cost']
                data.resources['money'] += data.MENU['latte']['cost']
                print(f"You paid too much. ${money_paid} is refunded.")
                print()
                print("Here's your espresso! Thanks for your business today!")


wants_a_drink = True
while wants_a_drink:
    action = input("What would you like? (espresso/latte/cappuccino?) ").lower()
    task(action)
    if action == "off":
        wants_a_drink = False

