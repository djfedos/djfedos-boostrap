#%%
# this fizzbuzz implementation doesn't use division (or modulus)

count_to = 100


def fizzbuzz(count_to = count_to):
    fizz = 1
    buzz = 1
    for unit in range(1, count_to + 1):
        if fizz == 3 and buzz == 5:
            print("Fizzbuzz")
            fizz = 1
            buzz = 1
        elif fizz == 3:
            print("Fizz")
            fizz = 1
            buzz += 1
        elif buzz == 5:
            print("Buzz")
            buzz = 1
            fizz += 1
        else:
            print(unit)
            fizz += 1
            buzz += 1



fizzbuzz()

# %%
# this fizzbuzz relies on modulus
count_to = 100


def fizzbuzz(count_to = count_to):
    for unit in range(1, count_to + 1):
        if unit % 3 == 0 and unit % 5 == 0:
            print("Fizzbuzz")
        elif unit % 3 == 0:
            print("Fizz")
        elif unit % 5 == 0:
            print("Buzz")
        else:
            print(unit)


fizzbuzz()

# %%
# TODO: fizzbuzz generalization

count_to = 100

numbers_and_phrases = {3:"Fizz", 5:"Buzz", 15:"Fizzbuzz"}  # edit and add more on your taste
# numbers_and_phrases = {3:"Fizz", 6:"Buzz", 12:"Fizzbuzz", 18:'Foozbeez'}  # see this as an example

# if number divides by x and by y, both phrases are written to output_list
# even if x and y are not coprimes
# uncomment an example below to check this behavior:
# numbers_and_phrases = {3:"Fizz", 7:"Buzz", 12:"Fizzbuzz", 18:'Foozbeez'}
 

descendind_numbers = list(numbers_and_phrases.keys())
descendind_numbers.sort(reverse=True)


def find_divisibles(descendind_numbers = descendind_numbers):
    divisibles = []
    rest_descending_numbers = descendind_numbers.copy()
    for num in descendind_numbers:
        rest_descending_numbers.remove(num)
        for divider in rest_descending_numbers:
            if num % divider == 0 and num not in divisibles:
                divisibles.append(num)
    return divisibles


divisibles = find_divisibles()


def find_non_divisibles(divisibles = divisibles, descendind_numbers = descendind_numbers):
    non_divisibles = []
    for num in descendind_numbers:
        if num not in divisibles:
            non_divisibles.append(num)
    return non_divisibles


non_divisibles = find_non_divisibles()


def fizzbuzz(count_to = count_to):
    output_list = []
    for item in range(1, count_to + 1):
        item_is_divisible = False
        what_we_output = ""

        if not item_is_divisible:
            for num in divisibles:
                if item % num == 0:
                    phrase = numbers_and_phrases.get(num)
                    what_we_output += f"{phrase} "
                    item_is_divisible = True
        if not item_is_divisible:
            for num in non_divisibles:
                if item % num == 0:
                    phrase = numbers_and_phrases.get(num)
                    what_we_output += f"{phrase} "
                    item_is_divisible = True
        if not item_is_divisible:
            what_we_output = item

        output_list.append(what_we_output)
    return output_list
        

fizzbuzz_output = fizzbuzz()

for item in fizzbuzz_output:
    print(item)


# %%
