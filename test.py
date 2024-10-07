import requests
import telebot


BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['weather'])
def inline(message):
    markup = telebot.util.quick_markup({
        'Singapore':{'callback_data': 'Singapore'}, # callback_data contains the long and lang of the location or the city name
        'Hong Kong':{'callback_data': 'Hong Kong'},
        'Others': {'callback_data': 'others'}
    }, row_width=1)
    bot.send_message(message.chat.id, 'Location?', reply_markup=markup)


@bot.callback_query_handler(lambda call: True)
def gather_params(call: telebot.types.CallbackQuery):
    if call.data == 'others':
        sent_message = bot.send_message(call.message.chat.id, "Enter the latitude and longitude of the desired location in the format \"latitude, longitude\"")
        bot.register_next_step_handler(sent_message, printing)
        return

    if call.data:
        printing(call.data)

def printing(inputs):
    if isinstance(inputs, str):
        print("it is a string")
        print(inputs)
    else:
        print("it is a message")
        print(inputs.text)

bot.infinity_polling()
