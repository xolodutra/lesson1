import ephem

# print(ephem.next_full_moon('2016-10-01'))

def fool_moon_metr(next_moon_question):
    # next_moon_question = input("введите сюда ваш вопрос о следующем полнолунии:__ ")
    valid_symbols = '1234567890/'
    old_str = next_moon_question
    new_str = ''
    for ch in old_str:
        if ch in valid_symbols:
            new_str += ch
    user_date = new_str
    fool_moon_date = str(ephem.next_full_moon(user_date))
    return fool_moon_date

    # str_user_date = "".join(user_date)
    # clear_user_date = str_user_date.split("?")
    # str_user_date = "".join(clear_user_date)
    # fool_moon_date = str(ephem.next_full_moon(str_user_date))
    # # print(fool_moon_date)
 
if __name__ == '__main__':
    print(fool_moon_metr('Когда ближайшее полнолуние 2016/10/01?'))
    # valid_symbols = '1234567890/'
    # old_str = 'Когда ближайшее полнолуние 2016/10/01?'
    # new_str = ''
    # for ch in old_str:
    #     if ch in valid_symbols:
    #         new_str += ch

    # print(new_str)