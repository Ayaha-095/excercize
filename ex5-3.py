import random


def get_max(*args):
    n_max = 0
    if len(args) != 0:
        for i in range(len(args)):
            if n_max < args[i]:
                n_max = args[i]
    else:
        n_max = 0
        return n_max
    return n_max


print(get_max(0, 4, 27, 7, 46))
