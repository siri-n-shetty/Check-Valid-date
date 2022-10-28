import time
today = datetime.datetime.today().date()
begin = datetime.date(2022,1,1)
num_days = (today - begin).days
print("The number of days ", num_days)