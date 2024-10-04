# The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.
# What is the difference between the year attribute and the isocalendar method?

from datetime import date

today = date.today()

# year attribute returns a year of that date
today_year = today.year
# isocalendar returns a named tuple where index of 0 gets you the year 
iso_year = today.isocalendar()[0]
print(iso_year)
# With named tuples can access values using attribute name rather than index 
iso_year = today.isocalendar()
print(iso_year.year)