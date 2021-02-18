from datetime import datetime

def retirement_calculator():
    retirement_age = int(input("Please enter the retirement age: "))
    client_age = int(input("Please enter Your age: "))
    other_condition = int(input("Please enter Your age: "))
    result = 0
    if (client_age + other_condition) < retirement_age:
        result = retirement_age - (client_age + other_condition)
    else:
        print("You are already retiree!")

    retirement_year = datetime.now().year + result

    print(f"{result} years left until retirement! It will be in {retirement_year}")


retirement_calculator()
