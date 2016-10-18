import ephem

# print(ephem.next_full_moon('2016-10-01'))

def fool_moon_metr():
    next_moon_question = input("введите сюда ваш вопрос о следующем полнолунии:__ ")
    user_input_to_list = next_moon_question.split(" ")
    print(user_input_to_list)
    i = 0
    for word in user_input_to_list:
        try:
            clear_user_date = user_input_to_list[i].split("?")
            print(int(clear_user_date))
            i = i + 1
        except (ValueError, TypeError):
            print("не число")
    # user_date = user_input_to_list[-1:]
    # str_user_date = "".join(user_date)
    # clear_user_date = str_user_date.split("?")
    # str_user_date = "".join(clear_user_date)
    # fool_moon_date = str(ephem.next_full_moon(str_user_date))
    # print(fool_moon_date)
    # return fool_moon_date



if __name__ == '__main__':
    # fool_moon_metr('Когда ближайшее полнолуние 2016/10/01?')
    fool_moon_metr()



# разбираем выражение слайсом по пробелу, 