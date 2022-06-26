# -*- coding: utf-8 -*-
from telebot import *
from telebot import types
import random
import day_pay
import sleep

#Параметр - токен необходимого бота с которым будем взаимодействовать
bot = telebot.TeleBot('')

#Метод для создания inline кнопок
def create_inline_button(list):
    markup = types.InlineKeyboardMarkup()
    button_list = [types.InlineKeyboardButton(text=x, callback_data=x) for x in list]
    markup.add(*button_list)
    return markup

#Метод для создания обычных кнопок
def create_button(list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button_list = [types.KeyboardButton(text=x) for x in list]
    keyboard.add(*button_list)
    return keyboard

#Отслеживаем команду /start
@bot.message_handler(commands=['start'])
def start(message):
    list = ['Да', 'Нет']
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
    bot.send_message(message.chat.id, name, parse_mode='html', reply_markup=create_inline_button(list))

@bot.callback_query_handler(func=lambda call: True)
def answer_inline(call):
    if call.data == "Да":
        list = ['Погода', 'Событие', 'Катя', 'Сколько дней осталось до зп?', 'Сколько осталось спать?', 'Насколько ты молодец']
        bot.send_message(call.message.chat.id, 'Отлично! Выбирай.', reply_markup=create_button(list))
    elif call.data == "Нет":
        bot.send_message(call.message.chat.id, 'Ответ неправильный. Давай еще раз... Нажимай на /start')
    elif call.data == "Пойду":
        bot.send_message(call.message.chat.id, sleep.sport_yes())
    elif call.data == "Не пойду":
        bot.send_message(call.message.chat.id, sleep.sport_no())

@bot.message_handler(content_types=['text'])
def choice_of_answer(message):
    if message.text == "Погода":
        list = ['Погода сегодня', 'Погода сейчас', 'Вернуться назад' ]
        bot.send_message(message.chat.id, 'Что именно тебя интересует?', reply_markup=create_button(list))
        bot.register_next_step_handler(message, weather)
    elif message.text == "Событие":
        list = ['Запланировать событие', 'Посмотреть событие', 'Вернуться назад']
        bot.send_message(message.chat.id, 'Что ты хочешь сделать?', reply_markup=create_button(list))
        bot.register_next_step_handler(message, event)
    elif message.text == "Катя":
        list = ['Открыть диалог с Катей', 'Открыть сообщение от Кати', 'Вернуться назад']
        bot.send_message(message.chat.id, 'Что ты хочешь сделать?', reply_markup=create_button(list))
        bot.register_next_step_handler(message, dialog_katya)
    elif message.text == "Сколько дней осталось до зп?":
        day = day_pay.day_salary()
        if day == 0:
            bot.send_message(message.chat.id, 'Сегодня ты получишь ЗП!!')
        else:
            bot.send_message(message.chat.id, 'Осталось: {}'.format(day))
    elif message.text == "Сколько осталось спать?":
        list = ['Пойду', 'Не пойду']
        bot.send_message(message.chat.id, 'Самое популярное занятие перед сном — считать, сколько часов ты проспишь, если уснешь прямо сейчас.'
                                          ' Как хорошо, что у тебя есть этот бот. \n'
                                          'Пойдешь завтра в зал?', reply_markup=create_inline_button(list))
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

# Делаем inline кнопку с ссылкой, для открытия диалога со мной в телеграме
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
