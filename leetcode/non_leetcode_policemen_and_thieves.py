def max_thieves_caught(array, k):
    policemen = {place for place in range(len(array)) if array[place] == 'P'}
    thieves = {place for place in range(len(array)) if array[place] == 'T'}
    cought = 0
    for policeman in policemen:
        if cought == len(policemen):
            return cought
        for distance in range(1, k+1):
            if policeman + distance in thieves:
                thieves.remove(policeman + distance)
                cought += 1
            elif policeman - distance in thieves:
                thieves.remove(policeman - distance)
                cought += 1
    return cought


if __name__ == '__main__':
    print(max_thieves_caught(['P', 'T', 'P', 'P', 'P', 'T'], 2))
