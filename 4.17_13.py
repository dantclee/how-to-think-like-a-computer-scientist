
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def intercept(x1, y1, x2, y2):
    slope_of_line = slope(x1, y1, x2, y2)
    return y1 - slope_of_line * x1

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

print('slope', slope(x1, y1, x2, y2))
print('y-intercept',intercept(x1, y1, x2, y2))
