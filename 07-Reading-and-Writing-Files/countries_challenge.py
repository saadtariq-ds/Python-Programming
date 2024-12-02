input_filename = "country_info.txt"

countries = {}
with open(file=input_filename, mode='r') as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split("|")
        country, capital, code, code3, dialing, timezone, currency =\
            data
        # print(country, capital, code, code3, dialing, timezone, currency,
        #       sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'country_code_3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict

# The challenge is to get a country name from the user, then display
# the capital city for the country
while True:
    chosen_country = input("Please enter the country name to check its capital: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        country_capital = country_data['capital']
        print(f"The capital of {chosen_country} is '{country_capital}'")
    elif country_key == "quit":
        break
