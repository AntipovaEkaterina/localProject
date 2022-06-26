"""
Сколько осталось спать
Условия:
1. Необходимо узнать, пойдет ли в спортзал пользователь завтра
2. Если пойдет в зал, то время подъема 7 утра
3. Если не пойдет в зал, то 8.30 утра (на самом деле 9 часов)
4. Необходимо учитывать день недели, так как если выходные дни, то подъем в 11 утра
5. Если на выходных решит пойти в зал, то подъем меняется на 9 утра
"""

from datetime import datetime
from datetime import timedelta

#Если завтра будний день
def workday(num):
    if num == 1:
        hour = timedelta(hours=7, minutes=00, seconds=00)
    else:
        hour = timedelta(hours=8, minutes=30, seconds=00)

    return hour

#Если завтра будет выходной
def weekend(num):
    if num == 1:
        hour = timedelta(hours=9, minutes=00, seconds=00)
    else:
        hour = timedelta(hours=11, minutes=00, seconds=00)

    return hour

#Если пользователь завтра идет в спортзал
def sport_yes():
    time_now = datetime.now()
    delta_1 = timedelta(hours=time_now.hour, minutes=time_now.minute, seconds=time_now.second)
    week_day = datetime.weekday(time_now)
    if week_day == 5 or week_day == 6:
        time = weekend(num=1) - delta_1
    else:
        time = workday(num=1) - delta_1

    return time

#Если не идет в зал
def sport_no():
    time_now = datetime.now()
    delta_1 = timedelta(hours=time_now.hour, minutes=time_now.minute, seconds=time_now.second)
    week_day = datetime.weekday(time_now)
    if week_day == 5 or week_day == 6:
        time = weekend(num=0) - delta_1
    else:
        time = workday(num=0) - delta_1

    return time
