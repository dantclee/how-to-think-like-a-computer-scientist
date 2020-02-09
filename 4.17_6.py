def days_in_month(month):
    month_and_days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
    'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
    try:
        return month_and_days[month]
    except:
        return None

name = input('Enter month: ')
print(days_in_month(name))
