# another python video course
#%%
# here will be a formatted string and string methods

first_name = "John"
last_name = "Smith"

statement = first_name + ' [' + last_name + '] is a coder'
formatted_statement = f'{first_name} [{last_name}] is a coder' # formatted string

print(formatted_statement == statement) # we can check if strings are equal!
print(statement.upper())
print(formatted_statement.lower())
print(statement.title())
print(statement.capitalize())
print(statement.find('is'))
print('is' in statement)
print(formatted_statement.replace('o', 'y'))


#%%
# car game

we_play = True
car_started = False
while we_play:
    user_command = input("> ").lower()
    if user_command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif user_command == "start":
        if not car_started:
            car_started = True
            print("Car started... Ready to go!")
        else:
            print("Car is already started")
    elif user_command == "stop":
        if car_started:
            car_started = False
            print("Car stopped")
        else:
            print("Car is already stopped")
    elif user_command == "quit":
        we_play = False
    else:
        print("I don't understand that...")

#%%
# a nested loop to generate 2D coordinates
x_size = int(input("Horizontal size: "))
y_size = int(input("Vertical size"))

for x in range(x_size):
    for y in range(y_size):
        print(f"({x}, {y})")

#%%
# nested loop challenge
# initially it was just one list and a code that's now inside a function

e_widthmap = [5, 2, 5, 2, 5]
l_widthmap = [2, 2, 2, 2, 5]
i_widthmap = [2, 2, 2, 2, 2]

def letter_of_letters(widthmap):
    for width in widthmap:
        line = ""
        xes = 0
        while xes < width:  # for xes in range(width) could do the same...
            line += "x"
            xes += 1
        print(line)
    print("")

letter_of_letters(e_widthmap)
letter_of_letters(l_widthmap)
letter_of_letters(i_widthmap)

# here I use nested loops explicitly. see less clunky implementation below
#%%
# three lines are enough here
# I suppose that string multiplication contains a loop inside,
# but not explicitly anyway

width_in_chars = [5, 2, 5, 2, 2]

for width in width_in_chars:
    print("x" * width)

 #%%
# find the max number in a list

list_of_numbers = [12, 5, 5, 51, 7, 48, 3, 11, 1.25, 33]

max_number = list_of_numbers[0]
for number in list_of_numbers:
    if number > max_number:
        max_number = number
print(max_number)

#%%
# remove duplicates from a list

list_with_dupes = [11, 2, 4, 11, 4, 5, 11, 7, 4, 2, 11, 13, 22]
list_without_dupes = list_with_dupes.copy()  # if we remove an item from original list,
for item in list_with_dupes:  # our code misses the next item not knowing the indexes have changed
    if list_without_dupes.count(item) > 1:
        list_without_dupes.remove(item)
print(list_without_dupes)

#%%
# remove duplicates from a list: a reference solution

list_with_dupes = [11, 2, 4, 11, 4, 5, 11, 7, 4, 2, 11, 13, 22]
list_without_dupes = []
for item in list_with_dupes:
    if item not in list_without_dupes:
        list_without_dupes.append(item)
print(list_without_dupes)

#%%
# unpacking demo

coordinates_tuple = (1, 2, 3)
coordinates_list = [4, 5, 6]

x, y, z = coordinates_tuple  # always give enough variables to unpack all the values
print(f"x = {x}, y = {y}, z = {z}")  # or else it will throw an error

a, b, c = coordinates_list  # works with lists and tuples as well
print(f"a = {a}, b = {b}, c = {c}")

#%%
