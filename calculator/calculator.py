# a calculator from a video course, now in separate file
# TODO: implement fetching data from files

import functools


def invalid_input_catch(func):
    @functools.wraps(func)
    def wrapper():
        try:
            return func()  # if we want decorator to return a value, use return keyword
        except ValueError:
            print("Invalid input: you should enter a number")
            return wrapper()  # if not a number, try again
    return wrapper


@invalid_input_catch
def get_num():
    num = float(input("Please enter a number "))
    return num


def get_op():
    op = input("Please specify the operation: +, -, *, / or ** ")
    while op not in ["+", "-", "*", "/", "**"]:
        print("You've entered a wrong operator, please retry")
        op = input("Please specify the operation: +, -, *, / or ** ")
    return op


num1 = get_num()

op = get_op()

num2 = get_num()


class CalcEngine():
    "A class to perform calculations with its static methods"
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def add_nums(num1, num2):
        print(num1 + num2)

    @staticmethod
    def substract_nums(num1, num2):
        print(num1 - num2)

    @staticmethod
    def multiply_nums(num1, num2):
        print(num1 * num2)

    @staticmethod
    def divide_nums(num1, num2):
        if num2 == 0:
            print("Don't try to divide by zero please")
        else:
            print(num1 / num2)

    @staticmethod
    def exponent(num1, num2):
        num2 = round(num2)
        print("Note that the power value is always rounded to a whole number")
        if num2 == 0:
            print(1)  # it's faster, isn't it?
        elif num2 > 0:
            exp_result = 1
            for i in range(num2):
                exp_result *= num1
            print(exp_result)
        else:
            inv_result = 1
            pos_num2 = -num2
            for i in range(pos_num2):
                inv_result *= num1
            exp_result = 1 / inv_result
            print(exp_result)


def apply_operator(op = op, num1 = num1, num2 = num2):
    if op == "+":
        CalcEngine.add_nums(num1, num2)
    elif op == "-":
        CalcEngine.substract_nums(num1, num2)
    elif op == "*":
        CalcEngine.multiply_nums(num1, num2)
    elif op == "**":
        CalcEngine.exponent(num1, num2)
    else:
        CalcEngine.divide_nums(num1, num2)


apply_operator()