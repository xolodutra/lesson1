from datetime import datetime
import csv

def output_reader(from_user, to_user, username ):

    # начинаем с добавления текущей даты
    dt_now = datetime.now()
    dt_now = dt_now.strftime('%d.%m.%Y  %H:%m')
    out_list = [dt_now]

    out_list.append(str(username))
    out_list.append(str(from_user))
    out_list.append(str(to_user))

    out_str = '\n{}'. format('\t'.join(out_list))
    with open('log_bot.csv', 'w', encoding='utf-8')  as logfile:
        fields = [date, time, username, content]
        writer = csv.DictReader(logfile, fields, delimiter =';' )
        
        logfile.write(out_str)

if __name__ == "__main__":
    output_reader("from_user", "to_user", "chat_out")