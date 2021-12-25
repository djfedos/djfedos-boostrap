#%%
# according to this tutorial: https://realpython.com/primer-on-python-decorators/
import functools


def my_first_decorator(func):
    def wrapper():
        print("An event before the function is called")
        func()
        print("An event after the function is called")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_first_decorator(say_whee)

say_whee()


@my_first_decorator
def say_hey():
    print("Hey")


say_hey()

# thus, decorators wrap functions, modifying their behavior, but not themselves

#%%
# a calculator from a video course, once again revisited.
# trying a decorator for catching invalid input
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
    num = float(input("Please enter a number"))
    return num


num1 = get_num()

op = input("Please specify the operation: +, -, *, / or **")
while op not in ["+", "-", "*", "/", "**"]:
    print("You've entered a wrong operator, please retry")
    op = input("Please specify the operation: +, -, *, / or **")

num2 = get_num()


def exponent(base, power):
    exp_result = 1
    for i in range(power):
        exp_result *= base
    return exp_result


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "**":
    print("Note that the power value is always rounded to a whole number")
    print(exponent(num1, round(num2)))  # our custom exponent written above
else:  # op == "/", all the other cases are excluded above
    if num2 == 0:
        print("Don't try to divide by zero please")
    else:
        print(num1 / num2)

#%%
# here we do it wrong


def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@do_twice
def greet(name):
    print(f"Hello, {name}")


greet("Kitty")  # unexpected argument

#%%
# and here we do it right


def do_twice(func):
    def wrapper(*args, **kwargs):  # now the wrapper takes any number of arguments
        func(*args, **kwargs)  # and passes it to func
        func(*args, **kwargs)
    return wrapper


@do_twice
def greet(name):
    print(f"Hello, {name}")


greet("Kitty")

#%%
# timing decorator: a stopwatch for function runtime
import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        runtime = end - start
        print(f"Finished {func.__name__!r} in {runtime:.4f} s")
        return value
    return wrapper


@timer
def slow_func(slowness):
    result = 0
    sum_or_squares = 0
    for num in range(slowness):
        for i in range(1000):
            sum_or_squares += (i**i)
        result += sum_or_squares
    return result


print(slow_func(10))
print(slow_func(100))


@timer
def waste_some_time(num_times):  # func from example: mine is slower
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(10)
waste_some_time(100)
waste_some_time(1000)  # slow_func(1000) runs longer than 42 s, beware

#%%
# debug decorator: useful for the functions we didn't write, but use
# if we run this code several times in here in notebook, it spits out dupes. why?
import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{key}={value!r}" for key, value in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value!r}")

        return value
    return wrapper


import math

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


print(approximate_e(10))

#%%
# a decorator to slow down our code
import time
import functools


def slow_down(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper


@slow_down
def countdown(seconds):
    if seconds < 1:
        print("Liftoff!")
    else:
        print(seconds)
        countdown(seconds - 1)


countdown(10)

#%%
