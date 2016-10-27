from datetime import datetime


def output_reader(output_log, chat_out):
    chat_out = {}
    # output_log =  ['first_name', 'text' ]
    output_log = []
    # начинаем с добавления текущей даты
    dt_now = datetime.now()
    dt_now = dt_now.strftime('%d.%m.%Y  %H:%m')
    out_list = [dt_now]
    i = 0
    # проходим по списку и находим каждый из его элементов в словаре, 
    # котоый выдаёт телеграм в update.message
    while i < len(output_log):
        och = output_log[i]
        log_info = chat_out.get(och)
        out_list.append(log_info)
        i = i + 1
        if i >= len(output_log):
            break
    out_str = '\n{}'. format('\t'.join(out_list) )

    with open('log_bot.txt', 'a', encoding='utf-8')  as logfile:
        logfile.write(out_str)


if __name__ == "__main__":
    output_reader("прпрпрп", "прпрпрп")



