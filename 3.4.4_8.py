
remind = 'Length must be a number.'
a = input('Enter length of first side of triangle (cm): ')
try:
    fa = float(a)
except:
    print(remind)
    quit()

b = input('Enter length of second side of triangle (cm): ')
try:
    fb = float(b)
except:
    print(remind)
    quit()

c = input('Enter length of the longest side of triangle (cm): ')
try:
    fc = float(c)
except:
    print(remind)
    quit()

sq_c = fc**2 # square of longest side
sum_sq_ab = fa**2 + fb**2 # sum of the squares of the remaining 2 sides

threshold = 1e-7
if abs(sq_c - sum_sq_ab) < threshold:
    print(True)
else:
    print(False)
