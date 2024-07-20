DRINKS = {
    'espresso': {
        'price': 150,
        'water': 50,
        'milk': 0,
        'coffee': 18,
    },
    'latte': {
        'price': 250,
        'water': 200,
        'milk': 150,
        'coffee': 24,
    },
    'cappuccino': {
        'price': 300,
        'water': 250,
        'milk': 100,
        'coffee': 24,
    },
}
machine_storage = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}


def can_make(drink):
    if machine_storage['water'] >= DRINKS[drink]['water']:
        if machine_storage['milk'] >= DRINKS[drink]['milk']:
            if machine_storage['coffee'] >= DRINKS[drink]['coffee']:
                return True
    return False


def print_report():
    print(f"Water: {machine_storage['water']} ml")
    print(f"Milk: {machine_storage['milk']} ml")
    print(f"Coffee: {machine_storage['coffee']} g")
    print(f"Profit: ${machine_storage['money'] / 100:.2f}")


def adjust_machine_storage(drink):
    machine_storage['water'] -= DRINKS[drink]['water']
    machine_storage['milk'] -= DRINKS[drink]['milk']
    machine_storage['coffee'] -= DRINKS[drink]['coffee']
    machine_storage['money'] += DRINKS[drink]['price']
    return machine_storage


def process_coins():
    money = 0
    print("Please insert your coins:")
    money += int(input("How many quarters? ")) * 25
    money += int(input("How many dimes? ")) * 10
    money += int(input("How many nickels? ")) * 5
    money += int(input("How many pennies? "))
    return money


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print_report()
    elif choice in DRINKS:
        if can_make(choice):
            payment = process_coins()
            if payment >= DRINKS[choice]['price']:
                change = payment - DRINKS[choice]['price']
                machine_storage = adjust_machine_storage(choice)
                print(f"Here is your {choice}. Enjoy!")
                if change > 0:
                    print(f"Here is ${change / 100:.2f} in change.")
            else:
                if DRINKS[choice]['milk'] >= machine_storage['milk']:
                    print(f"Low on milk")
                elif DRINKS[choice]['water'] >= machine_storage['water']:
                    print(f"Low on water")
                else:
                    print(f"Low on coffee")
        else:
            print("Sorry, we can't make that drink due to insufficient resources.")
    else:
        print("Invalid selection. Please choose from espresso, latte, or cappuccino.")
