def f2c(t):
    return round((t - 32) *5 // 9)

t = float(input('Enter Fahrenheit: '))
print(f2c(t))
