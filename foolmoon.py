import ephem

print(ephem.next_full_moon('2016-10-01'))

def fool_moon_metr():
    next_moon_question = input("введите сюда ваш вопрос о следующем полнолунии:__ ")
    user_input_to_list = next_moon_question.split(" ")
    print(user_input_to_list)
    user_date = user_input_to_list[-1:]
    print(user_date)
    str_user_date = "".join(user_date)
    int_user_date = list(str_user_date)
    print(int_user_date)
    clear_user_date = int_user_date.split("?")
    print(clear_user_date)
    # str_user_date = "".join(clear_user_date)
    # print(str_user_date)
    # fool_moon_date = ephem.next_full_moon(str_user_date)
    # print(fool_moon_date)



if __name__ == '__main__':
    fool_moon_metr()