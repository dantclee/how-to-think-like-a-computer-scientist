def turn_clockwise(letter):
    compass_points = ['N', 'E', 'S', 'W']
    letter_index = compass_points.index(letter)
    if letter_index == 3:
        next_compass_point = compass_points[0]
    else:
        next_compass_point = compass_points[letter_index + 1]
    return next_compass_point
point = input('Enter compass point: ')
print(turn_clockwise(point))
