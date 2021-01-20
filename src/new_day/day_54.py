import time


# def add(x, y):
#     print(x + y)
#
# def sub(x, y):
#     print(x - y)
#
# def mul(x, y):
#     print(x * y)
#
# def div(x, y):
#     print(int(x / y))
#
# def result(func, x, y):
#     return func(x, y)
#
# result(div, 5, 5)


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_hi():
    print("Hi")


@delay_decorator
def say_bye():
    print("Bye")


say_hello()

say_hi()

say_bye()
