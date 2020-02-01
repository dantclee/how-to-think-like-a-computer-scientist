def to_secs(hours, minutes, seconds):
    total_secs = 0
    total_secs = hours*60**2 + minutes*60 + seconds
    return total_secs

hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
seconds = int(input('Enter seconds: '))

print(to_secs(hours,minutes,seconds))
