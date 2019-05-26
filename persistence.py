def persistence(n, count = 0):
    if len(str(n)) == 1:
        return count
    mult =1
    count += 1
    for x in str(n):
        mult = mult * int(x)

    return persistence(mult, count)


print(persistence(3))