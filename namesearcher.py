import csv

month_dict = {'январе': 'январь',
              'феврале': 'февраль',
              'марте': 'март',
              'апреле': 'апрель',
              'мае': 'май',
              'июне': 'июнь',
              'июле': 'июль',
              'августе': 'август',
              'сентябре': 'сентябрь',
              'октябре': 'октябрь',
              'ноябре': 'ноябрь',
              'декабре': 'декабрь'}


def name_searcher(user_input):
    list_user_input = user_input.lower().split(" ")
    month = list_user_input[2]
    month = month_dict.get(month)
    year = list_user_input[3]

    with open('girl_names.csv', 'r', encoding='utf-8') as name_hisory:
        fields = ["system_object_id",
                  "global_id",
                  "NumberOfPersons",
                  "Year",
                  "Month",
                  "Name",
                  "ID"]

        pre_name_box = []
        name_box = []
        reader = csv.DictReader(name_hisory, fields, delimiter=';')
        for row in reader:
            year_birth = row.get('Year')
            month_birth = row.get('Month')
            girl_name = row.get('Name')
            if year_birth == year:
                if month_birth == month:
                    pre_name_box.append(girl_name)

        for item in range(5):
            name_box.append(pre_name_box[item])
            name_str = ' {}'. format(', '.join(name_box))

        return name_str

if __name__ == '__main__':
    name_searcher("пыщ")
