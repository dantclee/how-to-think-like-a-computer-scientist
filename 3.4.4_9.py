
remind = 'Length must be a number.'
sides = []
first_side = input('Enter length of first side of triangle (cm): ')
try:
    sides.append(float(first_side))
except:
    print(remind)
    quit()

second_side = input('Enter length of second side of triangle (cm): ')
try:
    sides.append(float(second_side))
except:
    print(remind)
    quit()

third_side = input('Enter length of the third side of triangle (cm): ')
try:
    sides.append(float(third_side))
except:
    print(remind)
    quit()

sides.sort()
#print('longest side is',sides[-1])
#quit()

sq_longest = sides[-1]**2 # square of longest side
sum_sq_remaining = sides[-2]**2 + sides[-3]**2 # sum of the squares of the remaining 2 sides

threshold = 1e-7
if abs(sq_longest - sum_sq_remaining) < threshold:
    print(True)
else:
    print(False)
