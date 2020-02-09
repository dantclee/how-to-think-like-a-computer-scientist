def day_num(name):
    name_of_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    try:
        number = name_of_day.index(name)
    except:
        number = None
    return number


day = input('Enter name of day: ')
print(day_num(day))
