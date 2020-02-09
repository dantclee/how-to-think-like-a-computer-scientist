def day_name(number):
    name_of_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    try:
        day = name_of_day[number]
    except:
        day = None
    return day

    
num = input('Enter number: ')
try:
    inum = int(num)
    print(day_name(inum))
except:
    print(None)
