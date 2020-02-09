num = input("Enter a number: ")
inum = int(num)
if inum > 1:
    for i in range(2, inum//2):
        if inum % i == 0:
            print(False)
            break
    else:
        print(True)
else:
    print(False)
