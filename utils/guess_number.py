def guess_number(number):
    intToGuess = 75
    if int(number) == intToGuess:
        return True
    elif int(number) > int(intToGuess):
        hot = 'more'
    else:
        hot = 'leser'
    return hot
