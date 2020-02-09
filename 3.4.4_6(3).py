list = ['ddd', 'sddfd','sam', 'sddfd']
count = 0
for _ in list:
    if _ != "sam":
        count += 1
    else:
        break
print(count)
