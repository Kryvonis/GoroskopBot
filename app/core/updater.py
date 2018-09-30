import os
import requests

from celery import Celery
from celery.schedules import crontab
from app.settings import Config


celery_cli = Celery('tasks', broker='redis://127.0.0.1:6379/0')


@celery_cli.task
def daily_t(*args):
    response = requests.get(Config.GOROSKOP_DAY)
    horoscope_name = f'{Config.BASE_PATH}/app/storage/daily.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded daily')


@celery_cli.task
def weekly_t(*args):
    response = requests.get(Config.GOROSKOP_WEEK)
    horoscope_name = f'{Config.BASE_PATH}/app/storage/weekly.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded weekly')


celery_cli.conf.beat_schedule = {
    'add-every-day': {
        'task': 'app.core.updater.daily_t',
        'schedule': crontab(hour=0, minute=0, day_of_week=1),
        # 'schedule': 5,
        'args': ('Hello',),
    },
    'add-every-week': {
        'task': 'app.core.updater.weekly_t',
        'schedule': crontab(hour=0, minute=0, day_of_week='monday'),
        # 'schedule': 10,
        'args': ('Hello',),
    },
}
