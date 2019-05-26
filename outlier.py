def find_outlier(integers):
    even_count = uneven_count = 0
    for x in integers:
        if x % 2 == 0:
            even_outlier = x
            even_count += 1
        elif x % 2 != 0:
            uneven_outlier = x
            uneven_count += 1
    if even_count == 1:
        return even_outlier
    return uneven_outlier