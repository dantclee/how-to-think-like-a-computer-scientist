def is_even(n):
    if n % 2 == 0:
        return True
    return False
    
def is_odd(n):
    return not is_even(n)

number = float(input('Enter a number: '))
print(is_odd(number))
