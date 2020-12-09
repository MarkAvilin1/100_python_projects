from src.coffee_machine.coffee_machine_OOP.finance_operations import process_coins
from src.coffee_machine.coffee_machine_OOP.make_coffee import make_coffee
from src.coffee_machine.coffee_machine_OOP.menu import resources, ORDER, profit, MENU
from src.coffee_machine.coffee_machine_OOP.sufficient import is_resource_sufficient
from src.coffee_machine.coffee_machine_OOP.transaction import is_transaction_successful

is_on = True

while is_on:
    choice = input("Что будете заказывать? (Эспрессо/Латте/Капучино): ")
    if choice not in ORDER:
        print("Пожалуйста, уточните ваш выбор напитка!")
    else:
        if resources["вода"] < 50:
            print("Закончилась Вода, запровляем и скоро вернемся! Извините за неудобство :(")
            break
        elif choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Вода: {resources['вода']}мл")
            print(f"Молоко: {resources['молоко']}мл")
            print(f"Кофе: {resources['кофе']}г")
            print(f"Деньги: {profit}р")
        else:
            drink = MENU[choice]

            if is_resource_sufficient(drink["ингредиенты"]):
                if choice == "эспрессо":
                    print(f"Из вас {MENU[choice]['цена']}р")
                elif choice == "латте":
                    print(f"Из вас {MENU[choice]['цена']}р")
                elif choice == "капучино":
                    print(f"Из вас {MENU[choice]['цена']}р")

                payment = process_coins()
                if is_transaction_successful(payment, drink["цена"], profit):

                    make_coffee(choice, drink["ингредиенты"])
