pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot('6001368822:AAFVqlAnIFp7ryFAt9-FXbWWxGYEtTU6Sl0')

from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я - Рандмуз, тестовый бот, по сути ничего из себя не представляющий", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Веселый)))')
        btn2 = types.KeyboardButton('Грустный(((')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Как ваше настроение сейчас?', reply_markup=markup)
    if message.text == 'Веселый)))':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Анекдот')
        bot.send_message(message.from_user.id, 'Че такой веселый? Хуй сосал вишневый?))))))))))'+'......'+'Ладно, не урчи) Хочешь анекдот в качестве извинений?', reply_markup=markup)
        markup.add(btn1)
    elif message.text == 'Грустный(((':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Анекдот')
        bot.send_message(message.from_user.id, 'Че такой грустный? Хуй сосал не вкусный?))))))))))''......'+'Ладно, не урчи) Хочешь анекдот в качестве извинений?', reply_markup=markup)
        markup.add(btn1)
    if message.text == 'Анекдот':
        markup = = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Давай, пока..')
        bot.send_message(message.from_user.id, 'Значит, заходят как-то в бар Адольф Гитлер, Джо байден, и негр...А бармен достает ружьё, и говорит: "О, у меня как раз три патрона!!"....И выстреливает все в негра ААХХАХАХАХАХАХАХАХАХАХХАХАХАХХАХАХАХА', reply_markup=markup)
        markup.add(btn1)
    if messge.text == 'Давай, пока..':
        markup = = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('👋 Поздороваться')
bot.polling(none_stop=True, interval=0)