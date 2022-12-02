import math


def middle_figure(a ,b):
    new_text = (a+b).replace(" ", "")
    if len(new_text) % 2 == 0:
        return 'no middle figure'
    else:
        middle =  math.ceil(len(new_text) / 2)
        return new_text[middle -1]


print(middle_figure('make love', 'not wars'))