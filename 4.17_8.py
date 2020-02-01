import math
def to_secs(hours, minutes, seconds):
    total_secs = hours*60**2 + minutes*60 + seconds
    return total_secs

hours = float(input('Enter hours: '))
minutes = float(input('Enter minutes: '))
seconds = float(input('Enter seconds: '))

print(math.trunc(to_secs(hours,minutes,seconds)))
