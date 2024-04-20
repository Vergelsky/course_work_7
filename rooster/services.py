# import json
# from datetime import datetime, timedelta
# from celery.schedules import crontab
#
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
#
# def create_iteration_task(task,
#                           days=1,
#                           name='Отправка напоминания пользователю',
#                           *args, **kwargs):
#     """
#     Создаёт объект повторяющейся задачи для celery-beat.
#     :param task: Путь к задаче, нарпимер: 'config.tasks.simple_task'
#     :param days: Частота повторения в днях
#     :param name: Имя задачи
#     :param args: Список для передачи в задачу
#     :param kwargs: Словарь для передачи в задачу
#     :return: Объект периодической задачи
#     """
#
#
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=days,
#         period=IntervalSchedule.DAYS,
#     )
#
#     periodic_task = PeriodicTask.objects.create(
#         interval=schedule,
#         name=name,
#         task=task,
#         args=json.dumps(args),
#         kwargs=json.dumps(kwargs),
#         expires=datetime.utcnow() + timedelta(seconds=30)
#     )
#
#     return periodic_task
