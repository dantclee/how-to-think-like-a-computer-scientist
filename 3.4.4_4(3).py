list = [1, 22, -232, -5, 7, 22333, -33233, 334444, 3333]
count = 0
for _ in list:
    if len(str(_)) == 5:
        count += 1
print(count)
