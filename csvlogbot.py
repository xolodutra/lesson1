import csv


with open('girl_names.csv', 'r', encoding='utf-8') as names:
    fields = ["system_object_id",
              "global_id",
              "NumberOfPersons",
              "Year",
              "Month",
              "Name",
              "ID"]

    reader = csv.DictReader(names, fields, delimiter=';')
    year_total = 0

    for row in reader:
        year_total = year_total + row['ID']
    print(year_total)
