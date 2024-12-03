import csv

cereals_filename = "cereal_grains.csv"

with open(file=cereals_filename, mode='r', encoding='utf-8',
          newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
