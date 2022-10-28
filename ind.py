import calendar
day = datetime.datetime(1947,8,15).weekday()
print("India became independent on ", day)
x = calendar.day_name[day]
print(x)