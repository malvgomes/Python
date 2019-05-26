def duplicate_count(text):
    count = 0
    chrs = []
    for x in text:
        if x not in chrs:
            if text.count(x) > 1:
            count += 1
        chrs.append(x)
    return count

print(duplicate_count('abcdead'))