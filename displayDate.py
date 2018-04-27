#Maia Reynolds
#4/25/18
#displayDate.py - prints date

from datetime import date

today=date.today()

weekdaynum=today.weekday()
day=today.day
monthnum=today.month
yearnum=today.year
weekday=["Monday,","Tuesday,","Wednesday,","Thursday,","Friday,","Saturday,","Sunday,"]
month=["January","February","March","April","May","June","July","August","September","October","November","December"]


print("Today is",weekday[weekdaynum],month[monthnum-1],day,yearnum)