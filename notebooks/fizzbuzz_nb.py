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
# fizzbuzz generalization
# I've got an insight on how this generalization should work
# not the way that I initially thought about

from math import gcd

count_to = 100

# example input dicts. feel free to play with them, edit and add more on your taste
# classic:
numbers_and_phrases = {3:"Fizz", 5:"Buzz", 15:"Fizzbuzz"}
# altered
# numbers_and_phrases = {3:"Fizz", 7:"Buzz", 21:"Fizzbuzz"}
# powers of two:
# numbers_and_phrases = {2:"Feez", 4:"Bazz", 8:"Fuzz", 16:"Booze", 32:"Baez", 64:"Bias""} 


# by default if ranks are equal, the program picks a largest suitable divider
# form numbers_and_phrases (as they are sorted in the desceding order)

# there also is a multiphrase mode that works this way:
# if a number divides to more than one number from our dict
# with the same rank, program prints not only a phrase of a
# largest divider, but all the phrases corresponding to dividers


# you can switch it to the multiphrase mode in the line below:
multiphrase_mode = False
# if you want multiple phrases only for dividers that are coprimes, switch it below:
multiphrase_coprimes_only = False

# uncomment examples below to check this behavior:
# numbers_and_phrases = {3:"Fizz", 7:"Buzz", 12:"Fizzbuzz", 18:'Foozbeez'}
# numbers_and_phrases = {3:"Fizz", 6:"Buzz", 12:"Fizzbuzz", 18:'Foozbeez'}

 
descendind_numbers = list(numbers_and_phrases.keys())
descendind_numbers.sort(reverse=True)

# the function below checks every number from our numbers_and_phrases dict
# if it is a product of some other numbers from this list. If it is,
# it counts how many pairs of multipliers from our list result in
# this number when multiplied (squares included)
# here I call this number of multiplier pairs and squares a rank 


def find_num_ranks(descendind_numbers = descendind_numbers):
    nums_with_ranks = {}
    rest_descending_numbers = descendind_numbers.copy()
    for num in descendind_numbers:
        rank = 0
        rest_descending_numbers.remove(num)
        rest_multipliers = rest_descending_numbers.copy()
        for first_multiplier in rest_descending_numbers:
            rest_multipliers.remove(first_multiplier)
            # should I count squares? not sure
            if num == first_multiplier * first_multiplier:
                rank += 1
            for second_multiplier in rest_multipliers:
                if num == first_multiplier * second_multiplier:
                    rank += 1
    
        nums_with_ranks.update({num:rank})

    return nums_with_ranks


nums_with_ranks = find_num_ranks()
nums = nums_with_ranks.keys()


def fizzbuzz(count_to = count_to):
    output_list = []
    for num in range(1, count_to + 1):
        what_we_output = ""
        nums_that_divide = []
        for this_one in nums:
            if num % this_one == 0:
                nums_that_divide.append(this_one)
        
        # here's the main trick:
        # from our nums we choose the one with highest rank
        # to print it's message instead of our number
        
        if nums_that_divide:
            num_with_max_rank = nums_that_divide[0]
            max_rank = nums_with_ranks.get(num_with_max_rank)
            for num_div in nums_that_divide:
                rank = nums_with_ranks.get(num_div)
                if rank > max_rank:
                   num_with_max_rank = num_div

            phrase = numbers_and_phrases.get(num_with_max_rank)
            what_we_output += f"{phrase} "

                # this feature implements the multiphrase mode:
                
            if multiphrase_mode:
                nums_that_divide_mpm = nums_that_divide.copy()
                nums_that_divide_mpm.remove(num_with_max_rank)
                if nums_that_divide_mpm:
                    for num_div_mpm in nums_that_divide_mpm:
                        rank_mpm = nums_with_ranks.get(num_div_mpm)
                        if rank_mpm == max_rank:
                            phrase = numbers_and_phrases.get(num_div_mpm)
                            if not multiphrase_coprimes_only:
                                what_we_output += f"{phrase} "
                            else:
                                if gcd(num_div_mpm, num_with_max_rank) == 1:
                                    what_we_output += f"{phrase} "

        if not nums_that_divide:
            what_we_output = num

        output_list.append(what_we_output)
    return output_list
        

fizzbuzz_output = fizzbuzz()

for item in fizzbuzz_output:
    print(item)

# %%
