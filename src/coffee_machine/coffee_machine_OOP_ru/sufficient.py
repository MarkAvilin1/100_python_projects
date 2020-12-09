from src.coffee_machine.coffee_machine_OOP.menu import resources


def is_resource_sufficient(order_ingredients):
    """Проверка, на хватку ингридиенотв"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Извинити не хватает ({item}).")
            return False
    return True
