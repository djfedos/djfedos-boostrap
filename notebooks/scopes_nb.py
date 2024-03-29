# %%
#based on the exercise from https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
from typing import Counter

from numpy.ma.core import not_equal


def scope_test():
    def do_local():
        spam = "local spam"
        print("In local scope, after local assignment:", spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print("Test spam: variable initialized as a", spam)
    do_local()
    print("In nonlocal scope, after local assignment:", spam)
    do_nonlocal()
    print("In nonlocal scope, after nonlocal assignment:", spam)
    do_global()
    print("In nonlocal scope, after global assignment:", spam)

scope_test()

print("In global scope, after global assignment:", spam)

# %%
# Closure according to https://medium.com/python-features/introduction-to-closures-in-python-8d697ff9e44d
def countdown(start):

    def display():
        n = start
        while n > 0:
            n -= 1
            print(n, 'left')
       
    return display

counter1 = countdown(3)
counter1()

del countdown

counter1()
countdown(3)

# %%
# how to throw errors on wrong input type (also in closure)
def takes_ints(some_input):

    def internal():
        if type(some_input) is int:
            print("thanks for the int")
        else:
            raise TypeError("wrong variable type, please give me an integer")
    return internal

tryout1 = takes_ints(100)
tryout1()

#to check out error raising, please uncomment two lines below this one:
#tryout2 = takes_ints("this is a string") 
#tryout2()

# %%
# closures with lists and dicts vs. integers and strings
# I don't quite get the difference, to be honest

def external(massive):

    def internal():
        if type(massive) == dict:
            print('OK, this is a dict')
            print('')
            for key, value in massive.items():
                print(key, ':', value)
                print('')
        elif type(massive) == list:
            print('OK, this is a list')
            print('')
            for ele in enumerate(massive):
                print(ele[0], ':', ele[1])
                print('')
        elif type(massive) == str:
            print('OK, this is a string')
            print('')
            print(massive)
            print('')
        elif type(massive) == float:
            print('OK, this is a floating point number')
            print('')
            print(massive)
            print('')
        else:
            print("I don't know the type of the input and how to deal with it")
            print('')
            print(massive)

      
    return internal

exampe_list = ["Asoka", "Bella", "Camilla", "Diana", "Elinor"]
some_list = external(exampe_list)
example_dict = {'Keyboards':'Jon Lord', 'Guitar':'Ritchie Blackmore', 'Bass':'Roger Glover', 'Drums':'Ian Paice', 'Vocals':'Ian Gillan'}
some_dict = external(example_dict)
some_str = external("Dict example above is Deep Purple MK II lineup, by the way")
some_float = external(0.25)
some_bool = external(True)

some_list()
some_dict()
some_str()
some_float()
some_bool()

# %%
# exercises on classes in Python from https://www.programiz.com/python-programming/class

class Person:
    "This is an example class" #the docstring that tells us  what the class is
    age = 10
    
    def greet(self):
        print("Hello")
    
print(Person.age)

print(Person.greet)

print(Person.__doc__)

Harry = Person()

Person.greet(Harry)


# %%
# more classes according to
# https://towardsdatascience.com/a-comprehensive-guide-for-classes-in-python-e6bb72a25a5e

class Book():
    "This is a class for books"
    def __init__(self, name, author, lenght_in_words):
        self.name = name
        self.author = author
        self.length_in_words = lenght_in_words

    # here we define what to print on print(object_of_Book_class) call
    def __str__(self):
        return "<" + self.name + " by " + self.author + ">"
    # here we make a method for our Book class. this is a function inside a class
    def page_number(self, font_size=12):
        length_in_words = self.length_in_words #local var length_in_words for page_number gets its value from the data attribute of the class
        words_per_page = 300 - (font_size - 12)*10
        return round(length_in_words/words_per_page)

b1 = Book("Pandas", "John Doe", 100000)

print(type(b1))
print("")

print(b1.name)
print(b1.author)
print(b1.length_in_words)
print("")

b1.name = "NumPy"
print("Book name from now is", b1.name)
print("")

# now we can call the method like this: object.method(parameter)
print("Page number with default 12 pt font is", b1.page_number())
print("Page number with 14 pt font is", b1.page_number(14))
print("Page number with 16 pt font is", b1.page_number(16))
print("Page number with 10 pt font is", b1.page_number(10))
print("Page number with 8 pt font is", b1.page_number(8))
print("")

print(b1)
# %%
# yet another class from 
# https://towardsdatascience.com/a-comprehensive-guide-for-classes-in-python-e6bb72a25a5e

class Book():
    "This is a class for books with class variables and instance variables"

    # class variables:
    page_width = 14
    cover_color = "blue"

    def __init__(self, name, author, lenght_in_words):
        self.name = name
        self.author = author
        self.length_in_words = lenght_in_words

    def __str__(self):
        return "<" + self.name + " by " + self.author + ">"

b2 = Book("Machine Learning", "Jane Doe", 120000)
b3 = Book("Humans Not Learning Anything", "Doe Janes", 128000)

print(b2.name, "by", b2.author)
print("Has a", b2.cover_color, "cover")
print("Pages are", b2.page_width, "cm wide")

print("")

print(b3.name, "by", b3.author)
print("Has a", b3.cover_color, "cover")
print("Pages are", b3.page_width, "cm wide")

print("")

b2.cover_color = "red"
print(b2.name, "by", b2.author, "now has a", b2.cover_color, "cover")

print("Meanwhile, for the Book class cover color remains", Book.cover_color)
print("")
# here's a child class for Book
class ColorBook(Book):
    def __init__(self, name, author, lenght_in_words, page_color, has_image):
        super().__init__(name, author, lenght_in_words) # Or we could write there Book instead of super(), a function that refers to the parent class
        self.page_color = page_color
        self.has_image = has_image

    # here I could override the def __str__(self) of the parent class, but I don't want to, I'd better leave it inherited for sake of illustration

c1 = ColorBook("Airbourne", "Bruce Dickinson", 66700, "blue", True)

print("Pages of the book", c1.name, "by", c1.author, "are", c1.page_color)
print("Its cover is", c1.cover_color, "and pages are", c1.page_width, "cm wide")
print(c1)
print("")

# %%
