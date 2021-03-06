from utils import guess_number


def binary_search(func, totalItems, mid=0, low=0, high=0, tryies=0):
    tryies = tryies + 1
    if mid == 0:
        high = totalItems

    mid = (low + high) / 2
    guess = func(mid)

    if guess != True:
        if guess == 'more':
            high = mid - 1
        else:
            low = mid + 1

        binary_search(func, totalItems, mid, low, high, tryies)
    else:
        print('searching item is', mid, 'total tryies', tryies)


binary_search(guess_number.guess_number, 100)
