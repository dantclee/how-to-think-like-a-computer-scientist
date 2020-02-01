def replace(s, old, new):
    list = s.split(old) # split the string with old as delimiter
    return new.join(list)

s = input('Enter string: ')
old = input('Enter old: ')
new = input('Enter new: ')

print(replace(s,old,new))
