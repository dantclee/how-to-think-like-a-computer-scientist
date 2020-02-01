import math
def hypotenuse(leg1,leg2):
    return math.sqrt(leg1**2 + leg2**2)

leg1 = float(input('Enter first leg: '))
leg2 = float(input('Enter second leg: '))

print(hypotenuse(leg1,leg2))
