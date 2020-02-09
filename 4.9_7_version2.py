def sum_to(n):
    """
    sum of all integers up to and including n.
    """
    return n*(n+1)/2

number = int(input('Enter an integer: '))
print(sum_to(number))
