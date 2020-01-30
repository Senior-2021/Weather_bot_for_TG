# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sqlite3


city_links = ['https://sinoptik.com.ru/погода-москва', 'https://sinoptik.com.ru/погода-астрахань', 'https://sinoptik.com.ru/погода-барнаул', 'https://sinoptik.com.ru/погода-владивосток', 'https://sinoptik.com.ru/погода-волгоград', 'https://sinoptik.com.ru/погода-воронеж-100472045', 'https://sinoptik.com.ru/погода-екатеринбург', 'https://sinoptik.com.ru/погода-ижевск', 'https://sinoptik.com.ru/погода-иркутск', 'https://sinoptik.com.ru/погода-казань', 'https://sinoptik.com.ru/погода-кемерово', 'https://sinoptik.com.ru/погода-краснодар', 'https://sinoptik.com.ru/погода-красноярск', 'https://sinoptik.com.ru/погода-липецк', 'https://sinoptik.com.ru/погода-махачкала', 'https://sinoptik.com.ru/погода-набережные-челны', 'https://sinoptik.com.ru/погода-нижний-новгород', 'https://sinoptik.com.ru/погода-новокузнецк', 'https://sinoptik.com.ru/погода-новосибирск', 'https://sinoptik.com.ru/погода-омск', 'https://sinoptik.com.ru/погода-оренбург', 'https://sinoptik.com.ru/погода-пенза', 'https://sinoptik.com.ru/погода-пермь', 'https://sinoptik.com.ru/погода-ростов-на-дону', 'https://sinoptik.com.ru/погода-рязань', 'https://sinoptik.com.ru/погода-самара-100499099', 'https://sinoptik.com.ru/погода-санкт-петербург', 'https://sinoptik.com.ru/погода-саратов', 'https://sinoptik.com.ru/погода-тольятти', 'https://sinoptik.com.ru/погода-томск', 'https://sinoptik.com.ru/погода-тюмень', 'https://sinoptik.com.ru/погода-ульяновск', 'https://sinoptik.com.ru/погода-уфа', 'https://sinoptik.com.ru/погода-хабаровск', 'https://sinoptik.com.ru/погода-челябинск', 'https://sinoptik.com.ru/погода-ярославль']
city_names = ['Москва' ,'Астрахань', 'Барнаул', 'Владивосток', 'Волгоград', 'Воронеж', 'Екатеринбург', 'Ижевск', 'Иркутск', 'Казань', 'Кемерово', 'Краснодар', 'Красноярск', 'Липецк', 'Махачкала', 'Набережные Челны', 'Нижний Новгород', 'Новокузнецк', 'Новосибирск', 'Омск', 'Оренбург', 'Пенза', 'Пермь', 'Ростов-на-Дону', 'Рязань', 'Самара', 'Санкт-Петербург', 'Саратов', 'Тольятти', 'Томск', 'Тюмень', 'Ульяновск', 'Уфа', 'Хабаровск', 'Челябинск', 'Ярославль']

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

for i in range(len(city_links)):
	url = city_links[i]
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')

	temp_now = soup.find(class_='weather__article_main_temp').contents[0]
	temp_max_min = soup.find(class_='weather__content_tab-temperature')
	temp_mm = temp_max_min.find_all('b')
	temp_min = temp_mm[0].contents[0]
	temp_max = temp_mm[1].contents[0]

	c.execute('''UPDATE weather SET temp_now="{}" WHERE city="{}" '''.format(temp_now, city_names[i]))
	c.execute('''UPDATE weather SET min_temp="{}" WHERE city="{}" '''.format(temp_min, city_names[i]))
	c.execute('''UPDATE weather SET max_temp="{}" WHERE city="{}" '''.format(temp_max, city_names[i]))
	conn.commit()

c.close()
conn.close()

