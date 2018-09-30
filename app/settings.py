# -*- encoding: utf-8 -*-
import os
import pathlib


class Config:
    # Flask settings

    BASE_PATH = pathlib.Path('.')

    DEBUG = os.getenv('DEBUG') == 'true'
    TESTING = os.getenv('TESTING') == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY')

    HOST = '127.0.0.1'
    PORT = 5000

    BOT_TOKEN = '670807539:AAFUCniw3aBwcwyT-Mm8oiqfuJUaFTvWjSw'
    BOT_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

    # SQL
    CREATE_TABLES = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_PATH.absolute()}/users.db'

    GOROSKOP_DAY = 'http://img.ignio.com/r/export/utf/xml/daily/com.xml'
    GOROSKOP_WEEK = 'http://ignio.com/r/export/utf/xml/weekly/cur.xml'
