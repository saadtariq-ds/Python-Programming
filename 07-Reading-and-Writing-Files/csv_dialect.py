import csv

input_filename = "country_info.txt"


with open(file=input_filename, mode='r', encoding='utf-8',
          newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)          # Reading from beginning of file
    reader = csv.reader(countries_data, dialect=country_dialect)
    for row in reader:
        print(row)

attributes = [
    'delimiter',
    'doublequote',
    'escapechar',
    'lineterminator',
    'quotechar',
    'quoting',
    'skipinitialspace'
]

for attribute in attributes:
    # print(f"{attribute}: {getattr(country_dialect, attribute)}")
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
