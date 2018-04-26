#Maia Reynolds
#4/25/18
#displayDate.py - prints date

from datetime import date

today=date.today()

weekdaynum=today.weekday()
weekday=["Monday,","Tuesday,","Wednesday,","Thursday,","Friday,","Saturday,","Sunday,"]

monthnum=today.month
month=["January","February","March","April"]


print("Today is",weekday[weekdaynum],month[monthnum])