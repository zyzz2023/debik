import telebot

bot = telebot.TeleBot('6001368822:AAFVqlAnIFp7ryFAt9-FXbWWxGYEtTU6Sl0')

from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я - Рандмуз, тестовый бот, по сути ничего из себя не представляющий", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Веселый)))')
        btn2 = types.KeyboardButton('Грустный(((')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Как ваше настроение сейчас?', reply_markup=markup)
    if message.text == 'Веселый)))':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Че такой веселый? Хуй сосал вишневый?))))))))))'+'......'+'Ладно, не урчи) Хочешь анекдот в качестве извинений?(Да/Нет)', reply_markup=markup)
    if message.text == 'Грустный(((':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Че такой грустный? Хуй сосал не вкусный?))))))))))''......'+'Ладно, не урчи) Хочешь анекдот в качестве извинений?(Да/нет)', reply_markup=markup)
    if message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Блин, ты странный, пока..')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Значит, заходят как-то в бар Адольф Гитлер, Джо байден, и негр...А бармен достает ружьё, и говорит: "О, у меня как раз три патрона!!"....И выстреливает все в негра ААХХАХАХАХАХАХАХАХАХАХХАХАХАХХАХАХАХА', reply_markup=markup)
    if message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Да')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,'Пидора ответ',reply_markup=markup)
    if message.text == 'Блин, ты странный, пока..':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Привет')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ну ладно(', reply_markup=markup)
bot.polling(none_stop=True, interval=0)