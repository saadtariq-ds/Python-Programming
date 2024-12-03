import csv

input_filename = "country_info.txt"

dialect = csv.excel
dialect.delimiter = "|"

countries = {}
with open(file=input_filename, mode='r', encoding='utf-8',
          newline='') as country_file:
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(country_file, delimiter=dialect.delimiter,
                                 fieldnames=headings)
    for row in dict_reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row


while True:
    chosen_country = input("Please enter the country name to check its capital: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        country_capital = country_data['capital']
        print(f"The capital of {chosen_country} is '{country_capital}'")
    elif country_key == "quit":
        break
