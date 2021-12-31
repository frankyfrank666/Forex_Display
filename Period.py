import datetime


def change_Time(x):
    end = datetime.date.today()

    if x == '1Y':
        time_change = datetime.timedelta(weeks=52)
    elif x == '6M':
        time_change = datetime.timedelta(weeks=26)
    elif x == '1M':
        time_change = datetime.timedelta(weeks=5)
    elif x == '2W':
        time_change = datetime.timedelta(weeks=2)
    else:
        time = datetime.datetime(2018, 1, 2)
        return time
    
    time =  (end - time_change)

    return time
