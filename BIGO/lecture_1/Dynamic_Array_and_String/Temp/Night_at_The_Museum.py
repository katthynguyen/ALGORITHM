wheel = input()

pointer = 'a'
count = 0

for c in wheel:
    distance = abs(ord(c) - ord(pointer))
    if distance < 13:
        count = count + distance
    else:
        count = count + (26 - distance)
    pointer = c
print(count)