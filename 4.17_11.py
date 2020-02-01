def compare(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

first_number = float(input('Enter first number: '))
second_number = float(input('Enter second number: '))
print(compare(first_number, second_number))
