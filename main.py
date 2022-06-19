# -*- coding: utf-8 -*-
from telebot import *
from telebot import types


#Параметр - токен необходимого бота с которым будем взаимодействовать
bot = telebot.TeleBot('')

#Отслеживаем команды
@bot.message_handler(commands=['start'])
def start(message):
    #Добавляем имя и фамилию пользоватея в сообщение с приветсвием
    name = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. Этот бот создан для тебя!'
    bot.send_message(message.chat.id, name, parse_mode='html')





bot.polling(none_stop=True)
