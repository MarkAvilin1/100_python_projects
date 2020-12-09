from src.coffee_machine.coffee_machine_OOP.menu import resources


def make_coffee(drink_name, order_ingredients):
    """Проверка хватки ингредиентов, в положительном случий выдается напиток."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Возьмите ваш {drink_name} ☕️. Приятного аппетита!")