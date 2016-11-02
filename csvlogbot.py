import csv


with open('girl_names.csv', 'r', encoding='utf-8')  as f:
    fields = ['system_object_id_','global_id_','NumberOfPersons_','Year','Month_','Name_','ID']
    # fields = [date, time, username, content]
    reader = csv.DictReader(f, fields, delimiter =';' )
    year_total = 0

    for row in reader:
        year_total = year_total + row['ID']
    print(year_total)
        # print(row)


