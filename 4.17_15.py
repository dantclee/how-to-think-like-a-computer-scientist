def is_odd(n):
    if n % 2 != 0:
        return True
    return False

number = float(input('Enter a number: '))
print(is_odd(number))
