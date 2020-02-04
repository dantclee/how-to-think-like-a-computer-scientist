def count(target, nested_list):
    """Returns the number of occurrenes of target in nested list"""
    frequency = 0
    for element in nested_list:
        if type(element) is list:
            frequency += count(target, element)
        elif element == target:
            frequency += 1
    return frequency


nested_list = [3, 4, 3, [3, 5, 9]]
target = 3
print(count(target,nested_list))
