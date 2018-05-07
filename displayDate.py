#Maia Reynolds
#4/25/18
#displayDate.py - prints date

from datetime import date #imports date

today=date.today() #makes variable today = the date today

day=today.day #makes day = the day of the month
year=today.year #makes year = to the year
weekday=["Monday,","Tuesday,","Wednesday,","Thursday,","Friday,","Saturday,","Sunday,"]#list of days
month=["January","February","March","April","May","June","July","August","September","October","November","December"]#list of months

#prints today's date
#takes the number of the day of the week it is (today.weekday()) from weekday, the list of days, and prints the word
#takes the month number (today.month)-1 because lists start at 0, from the list of months, and prints the word
print("Today is",weekday[today.weekday()],month[today.month-1],day,year)