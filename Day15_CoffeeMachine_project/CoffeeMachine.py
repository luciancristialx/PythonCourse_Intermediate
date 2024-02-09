from CoffeeMachineData import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#3. Print report
def format_report(profit):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${profit}"

def process_orders(choice):
    if choice != "off":
        return True
    else:
        return False


#Check resources sufficient
#4.a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
#4.b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “ Sorry there is not enough water.”
#4.c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources(choice, current_resources):
    choice_ingredients = MENU[choice]["ingredients"]
    for keys in choice_ingredients:
        if choice_ingredients[keys] > current_resources[keys]:
            print(f"Sorry there is not enough {keys}.")
            return False
        else:
            return True


#7. Make Coffee.
#7.a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
def use_resources(choice):
    choice_ingredients = MENU[choice]["ingredients"]
    for keys in choice_ingredients:
        resources[keys] -= choice_ingredients[keys]
    return resources

#5. Process coins.
#5.a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#5.b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#5.c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

#6. Check transaction successful?
#6.a. Check that the user has inserted enough money to purchase the drink they selected.E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “ Sorry that's not enough money. Money refunded. ”.
#6.b. If the user has inserted too much money, the machine should offer change.
def process_coins(menu_item):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if total < float(MENU[menu_item]["cost"]):
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > float(MENU[menu_item]["cost"]):
        change = total - float(MENU[menu_item]["cost"])
        print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {menu_item}☕. Enjoy!")
        return True


def get_price(menu_item):
    return float(MENU[menu_item]["cost"])

#1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
#1.a. Check the user’s input to decide what to do next.
#1.b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

#2.Turn off the Coffee Machine by entering “ off ” to the prompt.
#2.a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.

#6.c. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the
# profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

#7.b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
def coffee_machine():
    profit = 0
    should_continue = True
    while should_continue:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print(format_report(profit))
        elif user_input == "off":
            print(f"Have a nice day!")
            return
        else:
            continue_order = check_resources(user_input,resources)
            if continue_order:
                enough_money = process_coins(user_input)
                if enough_money:
                    use_resources(user_input)
                    profit += get_price(user_input)

coffee_machine()