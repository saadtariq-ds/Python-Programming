import csv

input_filename = "country_info.txt"

# with open(file=input_filename, mode='r', encoding='utf-8',
#           newline='') as countries_data:
#     reader = csv.reader(countries_data, delimiter='|')
#     for row in reader:
#         print(row)


# with open(file=input_filename, mode='r', encoding='utf-8',
#           newline='') as countries_data:
#     sample = countries_data.read()
#     country_dialect = csv.Sniffer().sniff(sample)
#     countries_data.seek(0)          # Reading from beginning of file
#     reader = csv.reader(countries_data, dialect=country_dialect)
#     for row in reader:
#         print(row)


with open(file=input_filename, mode='r', encoding='utf-8',
          newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)          # Reading from beginning of file
    reader = csv.reader(countries_data, dialect=country_dialect)
    for row in reader:
        print(row)
