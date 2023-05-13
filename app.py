import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "To start working with bot hit command in format:\n<Currancy name>" \
"<Convert to> \
<Summ converted currancy>\n Display all currency type: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Availble Currency:"
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise ConnectionError("Too many parameters")

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"User error.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Failed to process command\n{e}")
    else:
        text = f" Price {amount} {quote} in {base} is: {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling()