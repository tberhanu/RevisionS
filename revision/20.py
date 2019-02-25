""" 20. Represent 2 days, 6 hours, 15 minutes, and 40 seconds
        On top of that, add up 2 days and 6 hours
        Converting text to date
"""
from datetime import datetime, date, timedelta
d = timedelta(2, 6, 15, 40)
print(d)
d2 = timedelta(days=2,seconds=6)
print(d + d2)
date = datetime(2015, 5, 27)
print(date)
date3 = date + d2
print(date3)
print(datetime.now())

text = "2012-09-20"
text_to_date = datetime.strptime(text, '%Y-%m-%d')
print(text_to_date)

year, month, day = text.split("-")
print("Year: {0}, month: {1}, date: {2} ".format(year, month, day))
