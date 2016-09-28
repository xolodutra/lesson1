def cut_cake(parts):
    try:
        return 1/int(parts)
    except  (ZeroDivisionError, TypeError, ValueError):
        return "Вы с дуба рухнули?"
# cake = cut_cake(0)
cake = cut_cake("Пирожки горячие")

# def do_something(x):
#     try:
#         print(x)
#     except:
#         print('Привет')

    

# x = 0
# while x <10:
#     do_something(x)
# x += 1
