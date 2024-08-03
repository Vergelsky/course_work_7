# Курсовая работа по теме DRF и DOCKER
"Until the rooster pecks, the man will not cross himself"

API сервис для отправки уведомлений в телеграмм-бот о необходимости выполнить полезное действие, "привычку", которую мы пытаемся выработать. За выполненное действие возможно вознаграждающее действие.<br> 
Действия-"Привычки" и действия-вознаграждения создаются HTTP запросами.

поднимаем проект в докере:
docker-compose up


#### Регистрация польователя:
POST: /users<br>
{<br>
    "email": "user1@sky.pro",<br>
    "tg_id": 123456789,<br>
    "password": "1qaz2wsx"<br>
}

#### Получение токена:
POST: /token/<br>
{<br>
    "email": "user1@sky.pro",<br>
    "password": "1qaz2wsx"<br>
}<br>

#### Привычки текущего пользователя:
GET: /crossoneself/?page=1

#### Список публичных привычек:
GET: /public/

#### Создание привычки:
POST: /crossoneself/<br>
{<br>
    "period": 1,<br>
    "time": "11:11:11",<br>
    "action": "Действие привычки 1",<br>
    "duration": "11",<br>
}


#### Редактирование привычки с id=1:
UPDATE: /crossoneself/1/<br>
{<br>
    "action": "Новое действие привычки 1",<br>
}


#### Удаление привычки с id=1:
DELETE: /crossoneself/1/<br>

образец переменных окружения - в example_env
