import random


def random_data(number):
    a = random.sample('abcdefghijklmnopqrstuvwxyz0123456789', number)
    b = ''
    for i in a:
        b += i
    return b


