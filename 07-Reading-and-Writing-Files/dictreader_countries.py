import csv

input_filename = "country_info.txt"

countries = {}
with open(file=input_filename, mode='r', encoding='utf-8',
          newline='') as country_file:
    dict_reader = csv.DictReader(country_file, delimiter="|")
    for row in dict_reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row


while True:
    chosen_country = input("Please enter the country name to check its capital: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        country_capital = country_data['Capital']
        print(f"The capital of {chosen_country} is '{country_capital}'")
    elif country_key == "quit":
        break
