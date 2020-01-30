import telebot
import config
import sqlite3

bot = telebot.TeleBot(config.token)
city_names = ['Москва', 'Астрахань', 'Барнаул', 'Владивосток', 'Волгоград', 'Воронеж', 'Екатеринбург', 'Ижевск', 'Иркутск', 'Казань', 'Кемерово', 'Краснодар', 'Красноярск', 'Липецк', 'Махачкала', 'Набережные Челны', 'Нижний Новгород', 'Новокузнецк', 'Новосибирск', 'Омск', 'Оренбург', 'Пенза', 'Пермь', 'Ростов-на-Дону', 'Рязань', 'Самара', 'Санкт-Петербург', 'Саратов', 'Тольятти', 'Томск', 'Тюмень', 'Ульяновск', 'Уфа', 'Хабаровск', 'Челябинск', 'Ярославль']
keyboard = telebot.types.ReplyKeyboardMarkup(True)

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

for i in range(len(city_names)):
	keyboard.row(city_names[i])

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Выбери город в котором хочешь узнать погоду', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def mess(message):
	conn = sqlite3.connect('db.sqlite')
	c = conn.cursor()
	for i in range(len(city_names)):
		if message.text == city_names[i]:
			m = ''
			c.execute('''SELECT temp_now FROM weather WHERE city="{}"'''.format(city_names[i]))
			m += 'Температура на данный момент: '
			m += c.fetchone()[0].lstrip() + '\n'
			c.execute('''SELECT max_temp FROM weather WHERE city="{}"'''.format(city_names[i]))
			m += 'Максимальная температура сегодня: '
			m += c.fetchone()[0] + '\n'
			c.execute('''SELECT min_temp FROM weather WHERE city="{}"'''.format(city_names[i]))
			m += 'Минимальная температура сегодня: '
			m += c.fetchone()[0]
			bot.send_message(message.chat.id, m)


if __name__ == '__main__':
	bot.polling(none_stop=True)
