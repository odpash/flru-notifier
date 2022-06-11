import requests
import bs4
import telebot
from config import *


def parse_active_orders():
    req = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(req.text, features='lxml')
    print(soup.find('projects-list'))


def send_message_tg():
    Bot = telebot.TeleBot(token=tg_bot_token)
    Bot.send_message(my_tg_id, "Появился новый заказ!\n")


parse_active_orders()