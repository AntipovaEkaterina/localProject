"""
Сколько дней осталось до зарплаты
Условия:
1. Зарплата всегда выдается 28 числа каждого месяца
2. Если 28 число выпадает на субботу, то деньги выдают 27 числа
3. Если 28 число это воскресенье, то деньги выдают 29 числа
"""


import datetime

#Проверяем день недели, если суббота, то получаем в пятницу, а если воскременье, то получаем в понедельник. Возвращаем день выдачи зп
def weekday(weekday, day_sal):
    if weekday == 5:
        day_sal -= 1
    elif weekday == 6:
        day_sal += 1

    return day_sal

def day_salary():
    #Узнаем сегодняшнюю дату
    todays = datetime.datetime.today()

    #Дата выплаты в этом месяце
    day_sialary = datetime.date(year=todays.year, month=todays.month, day=28)

    #Если нынешняя дата больше даты получения зп, то считаем дни до даты выплаты зп следующего месяца
    if todays.day > day_sialary.day:
        num = datetime.date.weekday(datetime.date(year=todays.year, month=todays.month + 1, day=day_sialary.day)) #Проверяем, день недели даты в следующем месяце
        new_day = weekday(num, day_sialary.day) #Меняем число, если попадает на выходные
        day_sialary = datetime.date(year=todays.year, month=todays.month + 1, day=new_day) #Дата меняется, если попадает на выходные, если не попадает, то остается такой же
    #Считаем сколько дней осталось
    elif todays.day == day_sialary.day: #Если даты совпадают, то выплата сегодня
        print('Сегодня ты получишь деньги!!!!')

    retur = day_sialary - todays.date()

    return retur.days

