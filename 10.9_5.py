def recursive_min(nested_number_list):
    """Return the smallest value in a nested number list. Assume there are no empty
    lists or sublists"""
    smallest = None
    first_time = True
    for element in nested_number_list:
        if type(element) is list:
            value = recursive_min(element)
        else:
            value = element

        if first_time or value < smallest:
            smallest = value
            first_time = False

    return smallest

nested_list = [4, 5, [1, [0, 3]], 8, [7, 4]]
print(recursive_min(nested_list))
