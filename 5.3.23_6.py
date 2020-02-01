def scalar_mult(scalar, vector):
    scalar_multiple = []
    for value in vector:
        scalar_multiple.append(scalar * value)
    return scalar_multiple

scalar = int(input('Enter a scalar: '))
list_of_string = input('Enter a vector (value separated by ","): ').split(',')

#convert the list of strings above to a list of integers
list_of_int = list(map(int, list_of_string))
print(scalar_mult(scalar, list_of_int))
