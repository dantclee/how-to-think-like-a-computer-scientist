def reverse(string):
    return string[::-1]

def is_palindrome(string):
    if string == reverse(string):
        return True
    return False


string = input('Enter a string: ')
print(reverse(string))
print(is_palindrome(string))
