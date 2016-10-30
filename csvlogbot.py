import csv


with open('girl_names.csv', 'r', encoding='utf-8')  as f:
    fields = ['system_object_id_','global_id_','NumberOfPersons_','Year_','Month_','Name_','ID']
    # fields = [date, time, username, content]
    reader = csv.DictReader(f, fields, delimiter =';' )
    year_total = 0

    for row in reader:
        year_total += float(row['Year_'])
    print(year_total)


