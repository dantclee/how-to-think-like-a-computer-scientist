def swap(itemone,itemtwo):
    new_tuple = (itemtwo, itemone)
    return new_tuple

old_tuple = ('One', 'Two')

print(swap(*old_tuple))
