def turn_clockwise(letter):
    if letter == 'N':
        next_compass_point = 'E'
    elif letter == 'E':
        next_compass_point = 'S'
    elif letter == 'S':
        next_compass_point = 'W'
    elif letter == 'W':
        next_compass_point = 'N'
    else:
        next_compass_point = None
    return next_compass_point
point = input('Enter compass point: ')
print(turn_clockwise(point))
