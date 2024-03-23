import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
#Day count starts from 0
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year = 1992, month=10, day =24, hour = 21)
print(date_of_birth)