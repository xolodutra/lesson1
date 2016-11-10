import ephem


def fool_moon_metr(next_moon_question):
    valid_symbols = '1234567890/'
    old_str = next_moon_question
    new_str = ''
    for ch in old_str:
        if ch in valid_symbols:
            new_str += ch
    user_date = new_str
    fool_moon_date = str(ephem.next_full_moon(user_date))
    return fool_moon_date

if __name__ == '__main__':
    print(fool_moon_metr('Когда ближайшее полнолуние 2016/10/01?'))
