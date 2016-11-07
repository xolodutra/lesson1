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
    print(reader)
    for row in reader:
        print(row)
