import math

a = input('Enter length of base of triangle (cm): ')
try:
    fa = float(a)
except:
    print('Length must be a number.')
    quit()

b = input('Enter length of height of triangle (cm): ')
try:
    fb = float(b)
except:
    print('Height must be a number.')
    quit()

c = math.sqrt(fa**2 + fb**2)

print('Length of hypotenuse is',c,'cm.')
