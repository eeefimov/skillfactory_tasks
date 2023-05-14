import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "To start working with bot hit command in one line using format:\n<Currancy price you want to know>" \
"<Convert to> \
<Quantity of the first currency>\n Display all currency type: /values"
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
        val = message.text.split(" ")

        if len(val) != 3:
            raise ConnectionError("Should be only 3 parameters!")

        quote, base, amount = val
        quote = quote.capitalize()
        base = base.capitalize()
        total_base = CryptoConverter.get_price(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f"User error.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Failed to process command\n{e}")
    else:
        text = f" Price {amount} {quote} in {base} is: {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)