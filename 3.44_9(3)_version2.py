num = input("Enter a number: ")
inum = int(num)
if inum > 1:
    for i in range(2, inum//2):
        if inum % i == 0:
            print(inum, 'is not a prime number')
            break
    else:
        print(inum, 'is a prime number')
else:
    print(inum, 'is not a prime number')
