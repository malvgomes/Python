def delete_nth(order, max_e):
    number = []
    count = []
    nth = []
    for x in order:
        if x not in number:
            number.append(x)
            count.append(1)
            nth.append(x)
        else:
            if count[number.index(x)] <= max_e:
                count[number.index(x)] += 1
                nth.append(x)
    return nth

