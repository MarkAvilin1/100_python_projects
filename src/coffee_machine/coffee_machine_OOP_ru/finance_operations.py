def process_coins():
    """Возврошает сумму вводаных монеток"""
    print("Пожалуйста оплачивайте монетками!")
    total = int(input("сколько по 1 рубль?: ")) * 1
    total += int(input("сколько по 2 рубля?: ")) * 2
    total += int(input("сколько по 5 рублей?: ")) * 5
    total += int(input("сколько по 10 рублей?: ")) * 10
    return total
