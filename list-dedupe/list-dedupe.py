# this program can remove duplicates from a list
# there are two implementations
# TODO: fetching data from files, writing data to files

example_list_with_dupes = [11, 2, 4, 11, 4, 5, 11, 7, 4, 2, 11, 13, 22]

def dedupe(list_with_dupes):
    list_without_dupes = list_with_dupes.copy()  # if we remove an item from original list,
    for item in list_with_dupes:  # our code misses the next item not knowing the indexes have changed
        if list_without_dupes.count(item) > 1:
            list_without_dupes.remove(item)
    return list_without_dupes


def dedupe_reference(list_with_dupes):
    list_without_dupes = []
    for item in list_with_dupes:
        if item not in list_without_dupes:
            list_without_dupes.append(item)
    return list_without_dupes


        