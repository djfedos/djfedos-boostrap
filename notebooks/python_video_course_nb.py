# This notebook follows the video course: https://youtu.be/rfscVS0vtbw

#%%
# adding two numbers
num1 = float(input('Please enter a number:'))
num2 = float(input('Please enter another number'))
# how could I handle the wrong input, e.g. text? we'll see
result = num1 + num2
print(result)

#%%

is_male = False
is_tall = True

if is_male and is_tall:
    print("Here's a tall male")
elif is_male and not is_tall:
    print("Here's a short male")
elif not is_male and not is_tall:  # see, you can apply not keyword with no ()!
    print("Here's a short non-male")
else:
    print("Here's not a tall non-male")

#%%
# how to find a max number in a list of any length?


def max_num(num_list):
    current_max = num_list[0]
    for num in num_list:
        if num > current_max:
            current_max = num
    return current_max


print(max_num([2, 54, 23, 53, 132, 400, 4, 9, 75]))

# a better way than in the video, though in the video it shows ifs with comparisons
# so the purpose is different
#%%
# a better calculator: capable of processing two numbers at the time!

num1 = float(input("Please enter the first number"))
op = input("Please specify the operation: +, -, * or /")
num2 = float(input("Please enter the second number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Don't try to divide by zero please")
    else:
        print(num1 / num2)
else:
    print("You have entered a wrong operator, please retry")

#%%
# here I try to catch a wrong operator in real time, but surely I need
# something like while loop instead of recursion. Recursive function doesn't return
# a value, and there is a reason for it. Here I need to lurk more.

num1 = float(input("Please enter the first number"))


def get_op():
    op_we_get = input("Please specify the operation: +, -, * or /")
    if op_we_get not in ["+", "-", "*", "/"]:
        print("You've entered a wrong operator, please retry")
        get_op()
    else:
        return op_we_get


op = get_op()

num2 = float(input("Please enter the second number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Don't try to divide by zero please")
    else:
        print(num1 / num2)

#%%
# a better calculator with a while loop! and yes, it works as expected

num1 = float(input("Please enter the first number"))

op = input("Please specify the operation: +, -, * or /")
while op not in ["+", "-", "*", "/"]:
    print("You've entered a wrong operator, please retry")
    op = input("Please specify the operation: +, -, * or /")

num2 = float(input("Please enter the second number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:  # op == "/", all the other cases are excluded above
    if num2 == 0:
        print("Don't try to divide by zero please")
    else:
        print(num1 / num2)

#%%
# dict example
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Dec"])
print(monthConversions.get("Nov"))
print(monthConversions.get("Lol", "Not a valid Key"))

#%%
# Guessing Game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Guess the word")
        guess_count += 1
        guesses_left = guess_limit - guess_count
        if guesses_left == 1:
            print("You have 1 guess left")  # singular form
        else:
            print("You have", guesses_left, "guesses left")  # plural form
    else:
        out_of_guesses = True

if out_of_guesses:  # a more simple form of out_of_guesses == True
    print("You're out of guesses, you lose")
else:
    print("You've guessed it right, you win")

#%%
# a custom implementation of exponent using for loop


def exponent(base, power):
    exp_result = 1
    for time in range(power):
        exp_result *= base
    return exp_result


print(exponent(3, 4))  # expected output 81

#%%
# translator to Giraffe language


def giraffe_translate(phrase):
    translation = ""
    for char in phrase:
        if char in "aieou":
            translation += "g"
        elif char in "AIEOU":  # in the video capital letters are processed other way
            translation += "G"  # but I like to keep it simple like this
        else:
            translation += char
    return translation


print(giraffe_translate(input("Please, enter a phrase")))

#%%
# even better calculator with exponent and input error catching
import sys

try:
    num1 = float(input("Please enter the first number"))
except ValueError:
    print("Invalid input: you should enter a number")
    sys.exit(65)  # this is the correct way to interrupt the program execution

op = input("Please specify the operation: +, -, *, / or **")
while op not in ["+", "-", "*", "/", "**"]:
    print("You've entered a wrong operator, please retry")
    op = input("Please specify the operation: +, -, *, / or **")

try:
    num2 = float(input("Please enter the second number"))
except ValueError:
    print("Invalid input: you should enter a number")
    sys.exit(65)  # this is the correct way to interrupt the program execution

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
# reading from external file
# separate cells for every example
# doesn't always work

#%%
employees_txt = open("employees.txt", "r")

if employees_txt.readable():
    print(employees_txt.read())
else:
    print("File is not readable")

employees_txt.close()

#%%

employees_txt = open("employees.txt", "r")

if employees_txt.readable():
    print(employees_txt.readline())
else:
    print("File is not readable")

employees_txt.close()


#%%

employees_txt = open("employees.txt", "r")

if employees_txt.readable():
    print(employees_txt.readlines())
else:
    print("File is not readable")

employees_txt.close()

#%%

employees_txt = open("employees.txt", "r")

if employees_txt.readable():
    for employee in employees_txt.readlines():
        print(employee)
else:
    print("File is not readable")

employees_txt.close()

#%%
# writing to files

#%%
employees_txt = open("employees.txt", "a")  # append
employees_txt.write("\nToby - Human Resources")
employees_txt.close()

#%%
# here we create a new file with python program
# running it once more we can restore file's initial content
employees_txt = open("more_employees.txt", "w")
employees_txt.write("Kate - Software Engineer\n")
employees_txt.close()

#%%
# And here we overwright the file with a new content
employees_txt = open("more_employees.txt", "w")
employees_txt.write("Kim - CEO\n")
employees_txt.close()

#%%
# classes and objects

from Student import Student  # here we import a class from a file

student1 = Student("Jim", "Physics", 3.1, "False")
student2 = Student("Pam", "Chemistry", 2.3, "True")
print(student1.name, student1.gpa)
print(student2.name, student2.major)

#%%
# multiple choice quiz based on a class

class Question:
    def __init__(self, propmt, answer):
        self.prompt = propmt
        self.answer = answer


question_prompts = [
    "What color are apples?\n<a> Red/Green\n<b> Blue\n<c> Orange\n\n",
    "What color are beets?\n<a> Red/Green\n<b> Magenta\n<c> Yellow\n\n",
    "What color are tomatoes?\n<a> Teal\n<b> White\n<c> Red\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]


def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", score, "out of", len(questions), "correct")

ask_questions(questions)

#%%
# inheritance in classes

class Chef:

    def make_chicken(self):
        print("The chef cooks a chicken")

    def make_salad(self):
        print("The chef cooks a salad")

    def make_special(self):
        print("The chef cooks a bbq ribs")

myChef = Chef()


class ChineseChef(Chef):
    def make_special(self):
        print("The chef cooks orange chicken")

    def make_fried_rice(self):
        print("The chef cooks fried rice")


myChef.make_special()
myChineseChef = ChineseChef()
myChineseChef.make_special()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()







