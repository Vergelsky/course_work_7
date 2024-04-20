from datetime import datetime, timedelta

from celery import shared_task
import requests
from config.settings import BOT_TOKEN
from rooster.models import CrossOneself


@shared_task
def peck_all():
    """
    Отправляет уведомление пользователю
    если текущая дата больше или равна дате следующего выполнения и
    текущее время больше времени начала выполнения.
    И изменяет дату выполнения на следующую, в соответствии с периодом выполнения.
    :return:
    """
    token = BOT_TOKEN
    url = f'http://api.telegram.org/bot{token}/sendMessage'
    now = datetime.now()

    queryset = CrossOneself.objects.filter(is_nice=False)
    for co in queryset:
        run_time = co.time
        if now.date() >= co.next_run and now.time() > run_time:
            time = co.time
            action = co.action
            user_id = co.user.tg_id
            debug = f'\nПривычка: {co}\nДата сегодня:{now.date()},\n дата след.выолнения:{co.next_run}\n'
            message = f'Уже {time}! Пора делать {action}!{debug}'
            data = {'chat_id': user_id, 'text': message}

            response = requests.post(url, params=data)

            co.next_run = co.next_run + timedelta(days=co.period)
            co.save()

# @shared_task
# def periodic_peck(data_to_task):
#     token = BOT_TOKEN
#
#     time = data_to_task['time']
#     action = data_to_task['action']
#     user_id = data_to_task['user_id']
#
#     message = f'Уже {time}! Пора делать {action}!'
#
#     url = f'http://api.telegram.org/bot{token}/sendMessage'
#     data = {'chat_id': user_id, 'text': message}
#
#     response = requests.post(url, params=data)
#     print(response.json())
