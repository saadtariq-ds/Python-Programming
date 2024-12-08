import datetime
import locale

locale.setlocale(locale.LC_ALL)

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A, %d, %B, %Y')
print(pretty_start)

# Days
duration = datetime.timedelta(days=15)
end = start + duration
print(end)

print()

# Days and Hours
duration = datetime.timedelta(days=15, hours=4)
end = start + duration
print(end)

duration = datetime.timedelta(days=15, hours=48)
end = start + duration
print(end)

print()

d1 = datetime.timedelta(hours=2)
d2 = datetime.timedelta(minutes=120)
d3 = datetime.timedelta(seconds=7200)
print(d1, d2, d3, sep=', ')

print()

difference = end - start
print(repr(difference))
print(difference == duration)
