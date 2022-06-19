# -*- coding: utf-8 -*-
from telebot import *
from telebot import types


#Параметр - токен необходимого бота с которым будем взаимодействовать
bot = telebot.TeleBot('5345386610:AAFnp4VBTdh9o_7aFtx6We_N8hrpOAA7Ug4')

#Отслеживаем команды
@bot.message_handler(commands=['start'])
def start(message):
    #Добавляем имя и фамилию пользоватея в сообщение с приветсвием
    name = f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}.\n' \
           f'Благодаря этому боту ты сможешь узнать:</b>\n' \
           f'1.Погоду на сегодня\n' \
           f'2.Какая погода сейчас за окном\n' \
           f'3.Запланировать и посмотреть планы или событие\n' \
           f'4.Открыть диалог с Катей\n' \
           f'5.Какое сообщение вам оставила Катя\n' \
           f'6.Сколько дней осталось до зарплаты\n' \
           f'7.Сколько тебе осталось спать\n' \
           f'8.Насколько ты молодец\n' \
           f'<b>Скорее нажимай на кнопки и удивляйся моими способностями</b>'
    bot.send_message(message.chat.id, name, parse_mode='html')





bot.polling(none_stop=True)
