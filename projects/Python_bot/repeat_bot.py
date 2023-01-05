#pip install pytelegrambotapi

import telebot

bot = telebot.TeleBot('5664717377:AAFEkcO9HfzOGJbhWaRegwgxQaSR-UxuYPc')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Я от Ильшата. Напиши мне что-то")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "Вы написали: " + message.text)
    bot.send_message(message.chat.id, "Ильшат доволен, что все работает :)")

bot.polling(none_stop=True, interval=0)
