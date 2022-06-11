import requests
import bs4
import telebot
from config import *
import time

last_order_id = ""


def parse_active_orders():
    global last_order_id
    req = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(req.text, features='lxml')
    first_order = soup.find('div', {'class': 'b-post__grid'})
    first_order_a = first_order.find('a', {'class': 'b-post__link'})
    if first_order_a.get('id') != last_order_id:
        last_order_id = first_order_a.get('id')
        message = f"---------------------Появился новый заказ!---------------------\n" \
                  f"Ссылка: https://www.fl.ru{first_order_a.get('href')}\n" \
                  f"Цена: {str(first_order).split('сделка</a> ')[1].split('&nbsp;')[0]}\n" \
                  f"Название: {first_order_a.text}\n" \
                  f"""Описание: {str(first_order).split('b-post__txt ">')[1].split('</div>')[0]}"""
        send_message_tg(message)


def send_message_tg(message):
    Bot = telebot.TeleBot(token=tg_bot_token)
    Bot.send_message(my_tg_id, f"{message}")


while True:
    parse_active_orders()
    time.sleep(60)
