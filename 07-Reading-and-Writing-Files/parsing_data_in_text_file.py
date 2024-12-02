input_filename = "country_info.txt"

with open(file=input_filename, mode='r') as country_file:
    for row in country_file:
        data = row.strip('\n').split("|")
        print(data)
