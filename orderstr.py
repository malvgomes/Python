import re


def order(sentence):
    splitted = sentence.split()
    ordered = [None]*len(splitted)
    for x in splitted:
        ordered[int(re.findall("\d", x)[0]) - 1] = x
    return " ".join(ordered)

print(order("is2 Thi1s T4est 3a"))