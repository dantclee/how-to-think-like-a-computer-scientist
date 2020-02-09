def sum_to(n):
    """
    sum of all integers up to and including n.
    """
    total = 0
    while n>0:
        total += n
        n -= 1
    return total

number = int(input('Enter an integer: '))
print(sum_to(number))
