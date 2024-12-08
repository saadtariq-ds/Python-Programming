import datetime
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')  # French Location

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A, %d, %B, %Y')
print(pretty_start)

year = start.year
month = start.month
day = start.day

print(f"The {year} winter olympics started on day {day} of month {month}")

# Extracting Today's Date
today = datetime.date.today()
print(today)

# Extracting Day Name
print(today.strftime('%A'))

# Extracting Weekday Number
print(today.weekday())
