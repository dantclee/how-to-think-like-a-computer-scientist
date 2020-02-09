number = input('Enter a number: ')
n = int(number)
count = 0
if n > 0:
    while n > 0: # count the number of digits of positive number
        count += 1
        n = n // 10
elif n < 0:
    count += 1 # count the negative sign as a digit
    while abs(n) > 0: # count the number of digits of the absolute value
        count += 1
        n = abs(n) // 10
else:
    count = 1 # only 1 digit when n = 0
print(count)
