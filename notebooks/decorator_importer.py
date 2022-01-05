from decorators_module import do_twice


@do_twice
def greet(name):
    print(f"Hello, {name}!")


greet("Bob")

help(greet)  # to show functools effect
