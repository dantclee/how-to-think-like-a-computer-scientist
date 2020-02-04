def recursive_count(target, nested_list):
    """Returns the number of occurrenes of target in nested list
    This function is incomplete.
    """
    count = 0
    #if not nested_list:
    #    print('early_count: ', count)
    #    return count
    head, *tail = nested_list #Assign the first element of nested_list to head,
    #and the rest to tail.
    print('Head: ', head)
    print('Tail: ', tail)
    if isinstance(head, list):  # If head is a list....
        count += head.count(target)
    elif head == target:
        count += 1
        print('Count: ', count)
    else:
        print('Not target')
    recursive_count(target, tail)
    return count

nested_list = [3, 4, 5, [3, 5, 9]]
target = 3
print(recursive_count(target,nested_list))
