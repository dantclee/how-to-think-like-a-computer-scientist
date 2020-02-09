while True:
    hour = input("Hour (in 24-hour format): ")
    try:
        int_hour = int(hour)
        if int_hour < 1 or int_hour > 24:
            print("Hour between 1 and 24 (inclusive)")
        else:
            break
    except:
        print('Hour must be an integer')
wait_hour = int(input("Number of hours to wait: "))
remainder = wait_hour % 24
#print(remainder)
if int_hour + remainder > 24:
    alarm_time = int_hour + remainder - 24
else:
    alarm_time = int_hour + remainder
print(alarm_time)
