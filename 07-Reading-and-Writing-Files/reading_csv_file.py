import csv

csv_filename = "OlympicMedals_2020.csv"

with open(file=csv_filename, mode='r', encoding='utf-8',
          newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f"Column headers: {headers}")
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
