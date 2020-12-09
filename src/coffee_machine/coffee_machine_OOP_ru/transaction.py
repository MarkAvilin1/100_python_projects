
def is_transaction_successful(money_received, drink_cost, profit=None):
    """Проверка соответствие цены напитка с оплачивимой суммой"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Вам сдачи {change}р.")
        profit += drink_cost
        return True
    else:
        print("Извинете не хвотает денег. возврат.")
        return False
