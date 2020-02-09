def day_num(name):
    name_of_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    try:
        number = name_of_day.index(name)
    except:
        number = None
    return number

def day_name(number):
    name_of_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    try:
        day = name_of_day[number]
    except:
        day = None
    return day

def day_add(dayname, delta):
    index_dayname = day_num(dayname)
    increment = delta % 7
    index_returnday = index_dayname + increment
    return day_name(index_returnday)

name = input('Enter day: ')
if day_num(name) == None:
    print('Invalid day.')
    quit()
number = input('Enter number of holiday: ')
try:
    int_number = int(number)
    print(day_add(name,int_number))
except:
    print('Invalid number of holiday.')
