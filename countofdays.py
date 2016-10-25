from datetime import datetime, timedelta

def countdays():
    user_enter_date =  input("введи дату___")
    user_date = datetime.strptime(user_enter_date, '%d/%m/%Y')
    dt_now = datetime.now()
    dif_date = user_date - dt_now
    print(dif_date)
countdays()
