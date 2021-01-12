import COVID19Py
import telebot
from telebot import types
import os

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot(os.environ["Token"])


@bot.message_handler(commands=['start'])
def start(message):
    b = types.InlineKeyboardButton
    item_about = b(text='Обо мне', callback_data='about')
    markup_inline = types.InlineKeyboardMarkup(row_width=2).add(item_about)
    item_Russia = b(text='Ru', callback_data='Ru')
    item_German = b(text='De', callback_data='De')
    item_Ukraine = b(text='Ua', callback_data='Ua')
    item_Chehia = b(text='Cz', callback_data='Cz')
    item_france = b(text='Fr', callback_data='Fr')
    item_Italy = b(text='It', callback_data='It')
    item_USA = b(text='Us', callback_data='Us')
    item_Belgia = b(text='Be', callback_data='Be')
    markup_inline.add(item_Italy,item_USA,item_Belgia,
                      item_france,item_Ukraine,item_Russia,item_Chehia,item_German)

    bot.send_message(message.chat.id,
                     '<b>Привет!</b>👋\n✅Выберите код страны своего проживания\nЧтобы узнать больше нажми на кнопку "<b>Обо мне</b>"!⬇️',
                     reply_markup=markup_inline, parse_mode ="html" )




@bot.callback_query_handler(func=lambda call: True)
def hello(call):
    if call.data == "Ru":
        location = covid19.getLocationByCountryCode("RU")
        final_message = (
            f"<u>Данные по России</u>🇷🇺\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")
        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
    elif call.data == "De":
        location = covid19.getLocationByCountryCode("DE")
        final_message = (
            f"<u>Данные по Германии</u>🇩🇪\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли:</strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode= 'html')

    elif call.data == "Ua":
        location = covid19.getLocationByCountryCode("UA")
        final_message = (
            f"</u>Данные по Украине</u>🇺🇦\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
    elif call.data == "Cz":
        location = covid19.getLocationByCountryCode("CZ")
        final_message = (
            f"<u>Данные по Чехии</u>🇨🇿\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
    elif call.data == "Fr":
        location = covid19.getLocationByCountryCode("FR")
        final_message = (
            f"<u>Данные по Фрнации</u>🇫🇷\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
    elif call.data == "It":
        location = covid19.getLocationByCountryCode("IT")
        final_message = (
            f"<u>Данные по Италии</u>🇮🇹\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
    elif call.data == "Us":
        location = covid19.getLocationByCountryCode("US")
        final_message = (
            f"<u>Данные по Америке</u>🇺🇸\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
    elif call.data == "Be":
        location = covid19.getLocationByCountryCode("BE")
        final_message = (
            f"<u>Данные по Бельгии</u>🇧🇪\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']}\n☠️<strong>Погибли: </strong>{location[0]['latest']['deaths']}")

        bot.send_message(call.message.chat.id, final_message, parse_mode='html')


    elif call.data == "about":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_world = types.KeyboardButton('world')
        markup_reply.add(item_world)
        bot.send_message(call.message.chat.id,
                         '<b>Я коронабот!</b>\nМогу рассказать тебе про <u>статистику коронавируса</u>🦠\nДля этого просто напиши страну, про которую хочешь узнать🇷🇺\n<u>Или нажми на кнопку</u> ⬇️',
                         reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'world':
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>🌏\n🌡<b>Заболевших: </b>{location['confirmed']:,}\n☠️<b>Сметрей: </b>{location['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    elif get_message_bot == 'россия':
        location = covid19.getLocationByCountryCode("RU")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по России:</u>🇷🇺\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')


    elif get_message_bot == 'америка':
        location = covid19.getLocationByCountryCode("US")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Америке:</u>🇺🇸\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')


    elif get_message_bot == 'германия':
        location = covid19.getLocationByCountryCode("DE")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Германии:</u>🇩🇪\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    elif get_message_bot == 'италия':
        location = covid19.getLocationByCountryCode("IT")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Италии:</u>🇮🇹\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')


    elif get_message_bot == 'франция':
        location = covid19.getLocationByCountryCode("FR")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Франции:</u>🇫🇷\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')


    elif get_message_bot == 'бельгия':
        location = covid19.getLocationByCountryCode("BE")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Бельгии:</u> 🇧🇪\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    elif get_message_bot == 'чехия':
        location = covid19.getLocationByCountryCode("CZ")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Чехия:</u>🇨🇿\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')


    elif get_message_bot == 'украина':
        location = covid19.getLocationByCountryCode("UA")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по Украине:</u>\n" \
                        f"👨‍👩‍👧‍👧<b>Население: </b>{location[0]['country_population']}\n⏳<b>Последнее обновление: </b>{date[0]} {time[0]}\n🌡<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠️<b>Сметрей: </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')









while True:  
    try:
        bot.polling(none_stop=True)
    except OSError:
        bot.polling(none_stop=True)
