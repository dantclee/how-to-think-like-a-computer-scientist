def is_factor(f, n):
    if n % f == 0:
        return True
    return False

f = int(input('Enter factor: '))
n = int(input('Enter number: '))

print(f, 'is a factor of', n, ':', is_factor(f,n))
