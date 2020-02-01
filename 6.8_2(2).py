import numpy as np
#Use a mask to multiply all values below 100 in the following list by 2

a = np.array([230, 10, 284, 39, 76])

while True:
    a [a < 100] = a[a<100]*2
    if np.all(a > 100): #Repeat this until all values are above 100.
        break
#select all values between 150 < a < 200
print(a[(150 < a) & (a < 200)])
