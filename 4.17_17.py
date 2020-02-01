def is_factor(f, n):
    if n % f == 0:
        return True
    return False

def is_multiple(n, f):
    return is_factor(f, n)

f = int(input('Enter factor: '))
n = int(input('Enter number: '))

print(f, 'is a factor of', n, ':', is_factor(f,n))
print(n, 'is a multiple of', f, ':', is_multiple(n,f))
