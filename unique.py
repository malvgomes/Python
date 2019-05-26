def unique_in_order(iterable):
    unique = []
    for x in range(0, len(iterable)-1):
        if iterable[x] != iterable[x+1]:
            unique.append(iterable[x])

    unique.append(iterable[len(iterable)-1])
    return unique


print(unique_in_order([1,2,2,3,3]))
