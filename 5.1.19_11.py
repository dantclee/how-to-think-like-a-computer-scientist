def count(sub_str, string):
    count = 0
    start = 0
    while start < len(string):
        if string.find(sub_str, start) != -1:
            count += 1
            start = string.find(sub_str, start) + 1
        else:
            break
    return count

string = input('Enter a string: ')
sub_str = input('Enter a substring: ')
print(count(sub_str, string))
