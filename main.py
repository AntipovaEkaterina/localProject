# -*- coding: utf-8 -*-
from telebot import *
from telebot import types
import random

#Параметр - токен необходимого бота с которым будем взаимодействовать
bot = telebot.TeleBot('')

#Отслеживаем команду /start
@bot.message_handler(commands=['start'])
def start(message):
    #Добавляем InLine клавиатуру к сообщению
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Да", callback_data="yes")
    button2 = types.InlineKeyboardButton(text="Нет", callback_data="no")
    markup.add(button1, button2)
    #Добавляем имя и фамилию пользоватея в сообщение с приветсвием
    name = f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}.\n' \
           f'Благодаря этому боту ты сможешь узнать:</b>\n\n' \
           f'1.Погоду на сегодня\n' \
           f'2.Какая погода сейчас за окном\n' \
           f'3.Запланировать планы или событие\n' \
           f'4.Посмотреть планы на сегодня\n' \
           f'5.Открыть диалог с Катей\n' \
           f'6.Какое сообщение вам оставила Катя\n' \
           f'7.Сколько дней осталось до зарплаты\n' \
           f'8.Сколько тебе осталось спать\n' \
           f'9.Насколько ты молодец\n' \
           f'\n<b>Скорее нажимай на кнопки и удивляйся моими способностями\n\nТы готов(Да/Нет)?</b>'
    bot.send_message(message.chat.id, name, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer_inline(call):
    if call.data == "yes":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Погода')
        btn2 = types.KeyboardButton('Событие')
        btn3 = types.KeyboardButton('Катя')
        btn4 = types.KeyboardButton('Сколько дней осталось до зп?')
        btn5 = types.KeyboardButton('Сколько осталось спать?')
        btn6 = types.KeyboardButton('Насколько ты молодец')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, 'Отлично! Выбирай.', reply_markup=markup)
    if call.data == "no":
        bot.send_message(call.message.chat.id, 'Ответ неправильный. Давай еще раз... Нажимай на /start')

@bot.message_handler(content_types=['text'])
def choice_of_answer(message):
    if message.text == "Погода":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Погода сегодня')
        btn2 = types.KeyboardButton('Погода сейчас')
        btn3 = types.KeyboardButton('Вернуться назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Что именно тебя интересует?', reply_markup=markup)
        bot.register_next_step_handler(message, weather)
    elif message.text == "Событие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Запланировать событие')
        btn2 = types.KeyboardButton('Посмотреть событие')
        btn3 = types.KeyboardButton('Вернуться назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Что ты хочешь сделать?', reply_markup=markup)
        bot.register_next_step_handler(message, event)
    elif message.text == "Катя":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Открыть диалог с Катей')
        btn2 = types.KeyboardButton('Открыть сообщение от Кати')
        btn3 = types.KeyboardButton('Вернуться назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Что ты хочешь сделать?', reply_markup=markup)
        bot.register_next_step_handler(message, dialog_katya)

    elif message.text == "Сколько дней осталось до зп?":
        bot.send_message(message.chat.id, 'Скоро получишь! Осталось чуть-чуть')
    elif message.text == "Сколько осталось спать?":
        bot.send_message(message.chat.id, 'Самое популярное занятие перед сном — считать, сколько часов ты проспишь, если уснешь прямо сейчас.'
                                          ' Как хорошо, что у тебя есть этот бот.')
    elif message.text == "Насколько ты молодец":
        rand_num = random.randrange(85, 110, 1)
        if rand_num < 95:
            bot.send_message(message.chat.id, 'Ты молодец на {}%'.format(rand_num))
        else:
            bot.send_message(message.chat.id, 'Ты мега молодец на {}%'.format(rand_num))
    elif message.text == "Вернуться назад":
        start(message)
    else:
        bot.send_message(message.chat.id, 'Тут тебе придется немного подождать, я еще не все сделала.\n '
                                          'Поиграй пока с другими кнопками.<b> Для этого тебе надо нажать на /start</b>', parse_mode='html')


def weather(message):
    if message.text == "Погода сегодня":
        bot.send_message(message.chat.id, 'Сейчас расскажу тебе погоду в Новосибирске на сегодня')
        bot.register_next_step_handler(message, weather)
    elif message.text == "Погода сейчас":
        bot.send_message(message.chat.id, 'Сейчас расскажу тебе погоду в Новосибирске на данный момент')
        bot.register_next_step_handler(message, weather)
    elif message.text == "Вернуться назад":
        start(message)

def event(message):
    if message.text == "Запланировать событие":
        bot.send_message(message.chat.id, 'Напиши, что ты хочешь запланировать.')
        bot.register_next_step_handler(message, event)
    elif message.text == "Посмотреть событие":
        bot.send_message(message.chat.id, 'Что тебя интересует?')
        bot.register_next_step_handler(message, event)
    elif message.text == "Вернуться назад":
        start(message)

# Делаем кнопку с ссылкой, для открытия диалога со мной в телеграмме
def dialog_katya(message):
    if message.text == "Открыть диалог с Катей":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть диалог", url = ""))
        bot.send_message(message.chat.id, 'Жми, она ждет', reply_markup=markup)
        bot.register_next_step_handler(message, dialog_katya)
    elif message.text == "Открыть сообщение от Кати":
        bot.send_message(message.chat.id, 'Она просила передать тебе, что любит тебя и желает хорошего дня!')
        bot.register_next_step_handler(message, dialog_katya)
    elif message.text == "Вернуться назад":
        start(message)

bot.polling(none_stop=True)
