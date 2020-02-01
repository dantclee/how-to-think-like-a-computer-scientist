import math

def hours_in(seconds):
    return math.trunc(seconds // 60**2)

def minutes_in(seconds):
    return math.trunc((seconds % (60**2)) // 60)

def seconds_in(seconds):
    return (seconds % (60**2)) % 60

seconds = int(input('Enter seconds: '))
print('hours:',hours_in(seconds))
print('minutes:',minutes_in(seconds))
print('seconds:',seconds_in(seconds))
