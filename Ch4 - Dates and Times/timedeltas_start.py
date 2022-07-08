#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date
now = datetime.now()
print ("today is: " + str(now))


# TODO: print today's date one year from now
print ("one year from now it will be: " + str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print ("in four weeks and 3 days it will be: " + str(now + timedelta(weeks=4, days=3)))

# TODO: calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
today = date.today()
xmas = date(today.year, 12, 25)

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if xmas < today:
    print ("Christmas already went by %d days ago" % ((today-xmas).days))
    xmas = xmas.replace(year=today.year + 1)

# TODO: Now calculate the amount of time until April Fool's Day
time_to_xmas = xmas - today
print ("It's just", time_to_xmas.days, "days until Christmas!")
