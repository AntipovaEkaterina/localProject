# -*- coding: utf-8 -*-
from telebot import *
from telebot import types


#Параметр - токен необходимого бота с которым будем взаимодействовать
bot = telebot.TeleBot('')

#Отслеживаем команду /start
@bot.message_handler(commands=['start'])
def start(message):
    #Добавляем имя и фамилию пользоватея в сообщение с приветсвием
    name = f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}.\n' \
           f'Благодаря этому боту ты сможешь узнать:</b>\n' \
           f'1.Погоду на сегодня\n' \
           f'2.Какая погода сейчас за окном\n' \
           f'3.Запланировать планы или событие\n' \
           f'4.Посмотреть планы на сегодня\n' \
           f'5.Открыть диалог с Катей\n' \
           f'6.Какое сообщение вам оставила Катя\n' \
           f'7.Сколько дней осталось до зарплаты\n' \
           f'8.Сколько тебе осталось спать\n' \
           f'9.Насколько ты молодец\n' \
           f'<b>Скорее нажимай на кнопки и удивляйся моими способностями\n Ты готов(Да/Нет)?</b>'
    bot.send_message(message.chat.id, name, parse_mode='html')

#Отслеживаем сообщения пользователя. Создаем кнопки по полем ввода текста
@bot.message_handler(content_types=['text'])
def button(message):
    if message.text == "Да" or message.text == "да":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Погода сегодня')
        btn2 = types.KeyboardButton('Погода сейчас')
        btn3 = types.KeyboardButton('Запланировать событие')
        btn4 = types.KeyboardButton('Посмотреть событие')
        btn5 = types.KeyboardButton('Открыть диалог с Катей')
        btn6 = types.KeyboardButton('Открыть сообщение от Кати')
        btn7 = types.KeyboardButton('Сколько дней осталось до зп?')
        btn8 = types.KeyboardButton('Сколько осталось спать?')
        btn9 = types.KeyboardButton('Насколько ты молодец')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, 'Отлично! Выбирай.', reply_markup=markup)
    elif message.text == "Нет" or message.text == "нет":
        bot.send_message(message.chat.id, 'Ответ неправильный. Давай еще раз...')
    else:
        bot.send_message(message.chat.id, "Напиши, пожалуйста, Да или Нет")



bot.polling(none_stop=True)
