def flatten(nested_list):
    """Returns a simple list containing all values in a nested list"""
    simple_list = []
    for element in nested_list:
        if type(element) is list:
            simple_list.extend(element)
        else:
            simple_list.append(element)
    return simple_list


nested_list = [3, 4, 3, [3, 5, 9]]
print(flatten(nested_list))
