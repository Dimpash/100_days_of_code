
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


money = 0


# TODO: 1. Print report = func
def print_report():
    """ Print current resources """
    print("The current resource values:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 2. Check resources sufficient? = func
def check_resources_sufficient(coffee_recipe):
    """ Returns a message if resources are not sufficient """
    message = ""
    for resource_name in coffee_recipe:
        if coffee_recipe[resource_name] > resources[resource_name]:
            message += f"Sorry. There is not enough {resource_name}. "
    return message


# TODO: 3. Process coins = func
def process_coins():
    """ Get amount from coins """
    amount = int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.1
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01
    return amount

# TODO: 4. Check transaction successful = func


# TODO: 5. Make Coffee = func
def make_coffee(coffee_recipe):
    """Recalculates resources and money"""
    for resource_name in coffee_recipe['ingredients']:
        resources[resource_name] = resources[resource_name] - coffee_recipe['ingredients'][resource_name]
    global money
    money += coffee_recipe['cost']


# TODO: 6. Final func
def make_user_request():
    """ Makes one user order """
    is_working = True
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "report":
        print_report()
    elif coffee_type == "off":
        is_working = False
    elif coffee_type not in MENU:
        print("You input the wrong coffee type. Please try again.")
    else:
        coffee_recipe = MENU[coffee_type]
        not_enough_resources = check_resources_sufficient(coffee_recipe['ingredients'])
        if not_enough_resources != "":
            print(not_enough_resources)
        else:
            change = round(process_coins() - coffee_recipe['cost'], 2)
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if change > 0:
                    print(f"Here is {change} dollars in change")
                print(f"Here is your {coffee_type} ☕. Enjoy!")
                make_coffee(coffee_recipe)
    return is_working


next_request = True

while next_request:
    next_request = make_user_request()


