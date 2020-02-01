def remove_all(sub_str, string):
    start = 0
    remain_string = ''
    while start < len(string):
        if string.find(sub_str,start) != -1:
            index_start_sub_str = string.find(sub_str, start)
            remain_string += string[start:index_start_sub_str]
            start = string.find(sub_str,start) + len(sub_str)
        else:
            remain_string += string[start:]
            break
    return remain_string

string = input('Enter a string: ')
sub_str = input('Enter a substring: ')
print(remove_all(sub_str, string))
