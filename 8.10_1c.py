import calendar
import datetime

now = datetime.datetime.now()

year = input('Enter year: ')

if year:
    int_year = int(year)
else:
    int_year = int(now.year)

month = input('Enter month: ')

if month:
    int_month = int(month)
else:
    int_month = int(now.month)

try:
    calendar.prmonth(int_year,int_month)
except:
    print('Invalid month')
