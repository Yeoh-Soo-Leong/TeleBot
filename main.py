import os
import requests
import json
import telebot
# from telebot import types

from weather import get_weather_info

BOT_TOKEN = ""
WEATHERAPI_KEY = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message.chat.id, "testing")

# @bot.message_handler(commands=['all'])
# def menu(message):
#     print("in func menu")
#     button1 = telebot.types.KeyboardButton('/testing')
#     commands_keyboard = telebot.types.ReplyKeyboardMarkup([button1])
#     bot.send_message(message.chat.id, "Hi, these are your command options", reply_markup=commands_keyboard)

@bot.message_handler(commands=['json'])
def send_welcome(message):
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    bot.send_message(message.chat.id, "the name is {}".format(y['name']))
    bot.send_message(message.chat.id, y)

@bot.message_handler(commands=['weather'])
def inline(message):
    markup = telebot.util.quick_markup({
        'Singapore':{'callback_data': 'Singapore'}, # callback_data contains the long and lang of the location or the city name
        'Hong Kong':{'callback_data': 'Hong Kong'},
        'Others': {'callback_data': 'others'}
    }, row_width=1)
    bot.send_message(message.chat.id, 'Location?', reply_markup=markup)

@bot.callback_query_handler(lambda call: True)
def gather_params(call: telebot.types.CallbackQuery, message):
    if call.data == 'others':
        sent_message = bot.send_message(call.message.chat.id, "Enter the latitude and longitude of the desired location in the format \"latitude, longitude\"")
        bot.register_next_step_handler(sent_message, gather_params)
        return

    weather_json = get_weather_info(WEATHERAPI_KEY, call.data)
    
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())

    # # Print forecast
    # bot.send_message(call.message.chat.id, "Weather forecast at {} in {}".format(call.data, weather_json['location']['name']))

    # bot.send_message(call.message.chat.id, "CURRENT")
    # bot.send_message(call.message.chat.id, "{}\nTemperature: {}°C\nPrecipitation: {}mm".format(weather_json['current']['condition']['text'], weather_json['current']['temp_c'], weather_json['current']['precip_mm']))

    # bot.send_message(call.message.chat.id, "FORECAST")
    # bot.send_message(call.message.chat.id, "{}".format(weather_json['forecast']['forecastday'][0]['date']))
    # bot.send_message(call.message.chat.id, "Morning 8am\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][0]['hour'][8]['condition']['text'], weather_json['forecast']['forecastday'][0]['hour'][8]['temp_c'], weather_json['forecast']['forecastday'][0]['hour'][8]['precip_mm'], weather_json['forecast']['forecastday'][0]['hour'][8]['chance_of_rain']))
    # bot.send_message(call.message.chat.id, "Noon 12pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][0]['hour'][12]['condition']['text'], weather_json['forecast']['forecastday'][0]['hour'][12]['temp_c'], weather_json['forecast']['forecastday'][0]['hour'][12]['precip_mm'], weather_json['forecast']['forecastday'][0]['hour'][12]['chance_of_rain']))
    # bot.send_message(call.message.chat.id, "Evening 5pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][0]['hour'][17]['condition']['text'], weather_json['forecast']['forecastday'][0]['hour'][17]['temp_c'], weather_json['forecast']['forecastday'][0]['hour'][17]['precip_mm'], weather_json['forecast']['forecastday'][0]['hour'][17]['chance_of_rain']))

    # bot.send_message(call.message.chat.id, "{}".format(weather_json['forecast']['forecastday'][1]['date']))
    # bot.send_message(call.message.chat.id, "Morning 8am\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][1]['hour'][8]['condition']['text'], weather_json['forecast']['forecastday'][1]['hour'][8]['temp_c'], weather_json['forecast']['forecastday'][1]['hour'][8]['precip_mm'], weather_json['forecast']['forecastday'][1]['hour'][8]['chance_of_rain']))
    # bot.send_message(call.message.chat.id, "Noon 12pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][1]['hour'][12]['condition']['text'], weather_json['forecast']['forecastday'][1]['hour'][12]['temp_c'], weather_json['forecast']['forecastday'][1]['hour'][12]['precip_mm'], weather_json['forecast']['forecastday'][1]['hour'][12]['chance_of_rain']))
    # bot.send_message(call.message.chat.id, "Evening 5pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][1]['hour'][17]['condition']['text'], weather_json['forecast']['forecastday'][1]['hour'][17]['temp_c'], weather_json['forecast']['forecastday'][1]['hour'][17]['precip_mm'], weather_json['forecast']['forecastday'][1]['hour'][17]['chance_of_rain']))

def print_forecast(message, weather_json):
    bot.send_message(message.chat.id, "Weather forecast at {} in {}".format(call.data, weather_json['location']['name']))

    bot.send_message(message.chat.id, "CURRENT")
    bot.send_message(message.chat.id, "{}\nTemperature: {}°C\nPrecipitation: {}mm".format(weather_json['current']['condition']['text'], weather_json['current']['temp_c'], weather_json['current']['precip_mm']))

    bot.send_message(message.chat.id, "FORECAST")
    bot.send_message(message.chat.id, "{}".format(weather_json['forecast']['forecastday'][0]['date']))
    bot.send_message(message.chat.id, "Morning 8am\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][0]['hour'][8]['condition']['text'], weather_json['forecast']['forecastday'][0]['hour'][8]['temp_c'], weather_json['forecast']['forecastday'][0]['hour'][8]['precip_mm'], weather_json['forecast']['forecastday'][0]['hour'][8]['chance_of_rain']))
    bot.send_message(message.chat.id, "Noon 12pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][0]['hour'][12]['condition']['text'], weather_json['forecast']['forecastday'][0]['hour'][12]['temp_c'], weather_json['forecast']['forecastday'][0]['hour'][12]['precip_mm'], weather_json['forecast']['forecastday'][0]['hour'][12]['chance_of_rain']))
    bot.send_message(message.chat.id, "Evening 5pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][0]['hour'][17]['condition']['text'], weather_json['forecast']['forecastday'][0]['hour'][17]['temp_c'], weather_json['forecast']['forecastday'][0]['hour'][17]['precip_mm'], weather_json['forecast']['forecastday'][0]['hour'][17]['chance_of_rain']))

    bot.send_message(message.chat.id, "{}".format(weather_json['forecast']['forecastday'][1]['date']))
    bot.send_message(message.chat.id, "Morning 8am\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][1]['hour'][8]['condition']['text'], weather_json['forecast']['forecastday'][1]['hour'][8]['temp_c'], weather_json['forecast']['forecastday'][1]['hour'][8]['precip_mm'], weather_json['forecast']['forecastday'][1]['hour'][8]['chance_of_rain']))
    bot.send_message(message.chat.id, "Noon 12pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][1]['hour'][12]['condition']['text'], weather_json['forecast']['forecastday'][1]['hour'][12]['temp_c'], weather_json['forecast']['forecastday'][1]['hour'][12]['precip_mm'], weather_json['forecast']['forecastday'][1]['hour'][12]['chance_of_rain']))
    bot.send_message(message.chat.id, "Evening 5pm\n{}\nTemperature: {}°C\nPrecipitation: {}mm\nChance of rain: {}%".format(weather_json['forecast']['forecastday'][1]['hour'][17]['condition']['text'], weather_json['forecast']['forecastday'][1]['hour'][17]['temp_c'], weather_json['forecast']['forecastday'][1]['hour'][17]['precip_mm'], weather_json['forecast']['forecastday'][1]['hour'][17]['chance_of_rain']))



bot.infinity_polling()
