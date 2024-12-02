input_filename = "country_info.txt"

# with open(file=input_filename, mode='r') as country_file:
#     for row in country_file:
#         data = row.strip('\n').split("|")
#         country, capital, code, code3, dialing, timezone, currency =\
#             data
#         print(country, capital, code, code3, dialing, timezone, currency,
#               sep='\n\t')

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

print(countries)
