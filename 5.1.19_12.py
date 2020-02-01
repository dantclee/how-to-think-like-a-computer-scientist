def remove(sub_str, string):
    if string.find(sub_str) != -1:
        index_start_sub_str = string.find(sub_str)
        index_after_sub_str = string.find(sub_str) + len(sub_str)
        firststring = string[:index_start_sub_str]
        secondstring = string[index_after_sub_str:]
        return firststring + secondstring
    else:
        return string

string = input('Enter a string: ')
sub_str = input('Enter a substring: ')
print(remove(sub_str, string))
