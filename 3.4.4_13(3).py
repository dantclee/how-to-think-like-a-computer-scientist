number = input('Enter a number: ')
n = abs(int(number))
count = 0
while n != 0:
    digit = n % 10 # assign the last digit from the right to variable digit
    if digit % 2 == 0:
        count = count + 1
    n = n // 10 # erase the digit just checked
print(count)
