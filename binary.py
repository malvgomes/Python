def countBits(n):
    count = 0
    for x in str(bin(n))[2:]:
        if int(x) == 1:
            count += 1
    return count

print(countBits(1234))
