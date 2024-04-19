# Курсовая работа по теме DRF

"Until the rooster pecks, the man will not cross himself"

#### Регистрация польователя:
POST: /user/<br>
{<br>
    "username": "user1",<br>
    "password": "1qaz2wsx"<br>
}

#### Получение токена:
POST: /token/<br>
{<br>
    "username": "user3",<br>
    "password": "1qaz2wsx"<br>
}<br>

#### Привычки текущего пользователя:
GET: /crossoneself/

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