# Курсовая работа по теме DRF

"Until the rooster pecks, the man will not cross himself"

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