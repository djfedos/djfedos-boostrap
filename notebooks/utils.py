def find_max(list_of_numbers:list):
    max_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number > max_number:
            max_number = number
    return(max_number)