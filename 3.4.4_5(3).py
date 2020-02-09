list = [1, 59, 7, 22333]
sum = 0
for _ in list:
    if _ % 2 == 1:
        sum += _
    else:
        break
print(sum)
