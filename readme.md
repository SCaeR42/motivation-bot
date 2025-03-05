# Мотивашкин
*Telegram Bot для отправки мотивационных сообщений*

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://choosealicense.com/licenses/mit/) [![version](https://img.shields.io/badge/version-1.0-blue)](https://img.shields.io/badge/version-1.0-blue)


Этот проект представляет собой Telegram бота, который отправляет мотивационные сообщения пользователям по расписанию. Пользователи могут настроить интервал между сообщениями, а также активировать и деактивировать отправку сообщений через команды в чате.

## Алгоритм работы:

- Пользователь подключается к боту.
- Бот предлагает выбрать интервал получения сообщений.
- Бот сохраняет настройки пользователя.
- По заданному расписанию бот запрашивает у Python-скрипта случайное сообщение.
- Отправляет пользователю сообщение в соответствии с его настройками.


## Что понадобится:

- Aiogram (или python-telegram-bot) — для работы с Telegram API.
- APScheduler — для отправки сообщений по расписанию.
- База данных (например, SQLite) — для хранения настроек пользователей.
- Скрипт Python — для генерации случайного сообщения.


## Как будем делать?

- Настроим Telegram-бота через BotFather.
- Напишем Python-скрипт, который будет отдавать случайное сообщение.
- Сделаем обработчик команд (/start, /settings).
- Реализуем хранение настроек пользователя.
- Добавим планировщик, который будет отправлять сообщения по заданному интервалу.


## Функции бота

- Отправка случайных мотивационных сообщений.
- Настройка интервала между сообщениями (минуты, часы).
- Возможность остановить отправку сообщений.
- Использует SQLite для хранения настроек пользователей.
- Работает с библиотеками `aiogram` для взаимодействия с Telegram API и `apscheduler` для управления расписанием задач.

## DEMO
Посмотреть действующую версию бота можно тут [@PositivizerBot](https://t.me/PositivizerBot)

## Структура проекта
```
. ├── main.py # Основной файл с кодом бота 
  ├── config.py (config.example.py) # Конфигурационный файл для хранения токена 
  ├── message_generator.py # Генератор мотивационных сообщений 
  ├── users.db # База данных SQLite для хранения настроек пользователей 
  └── README.md # Этот файл
```

## Установка

### Требования

- Python 3.7 и выше
- Установленные библиотеки:
  - `aiogram`
  - `apscheduler`
  - `sqlite3`

### Установка зависимостей

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/yourusername/motivation-bot.git
   cd motivation-bot
```

2. Создайте виртуальное окружение:

```bash
python3 -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Создайте файл config.py и добавьте свой токен бота:

```bash
TOKEN = "ваш_токен_бота
```

## Создание базы данных

База данных users.db будет автоматически создана при первом запуске бота.


## Использование

1. Запустите бота:
```bash
python main.py
```

2. В Telegram найдите своего бота и отправьте команду `/start`.

3. Для настройки интервала отправки сообщений отправьте команду `/settings`. Выберите один из предложенных интервалов:

- 1 час
- 3 часа
- 6 часов
- 12 часов
- 24 часа

4. Чтобы остановить отправку сообщений, выберите опцию "Остановить отправку сообщений".

## Использование systemd (для постоянной работы)

1. Создайте unit-файл для вашего бота:
```Bash
sudo nano /etc/systemd/system/motivation-bot.service
```
2. Добавьте следующее содержимое:
```Bash
[Unit]
Description=Motivation Telegram Bot
After=network.target

[Service]
User=YOUR_USER
WorkingDirectory=/home/YOUR_USER/motivation-bot
ExecStart=/home/YOUR_USER/motivation-bot/venv/bin/python /home/YOUR_USER/motivation-bot/main.py
Restart=always

[Install]
WantedBy=multi-user.target

```
*Замените your_user на вашего пользователя.*

3. Перезагрузите systemd и включите сервис:
```Bash
sudo systemctl daemon-reload
sudo systemctl enable motivation-bot
sudo systemctl start motivation-bot
```

4. Чтобы проверить статус:
```Bash
sudo systemctl status motivation-bot
```

5. Ожидание работы бота

Теперь бот должен работать в фоновом режиме на вашем сервере VPS. Если возникнут ошибки, вы сможете их отследить через логи с помощью команды:
```Bash
journalctl -u motivation-bot -f
```

Это позволяет вам отслеживать вывод бота в реальном времени.


## Разработка

Если вы хотите внести изменения в проект, используйте следующие команды для работы с Git:

Клонировать репозиторий:
```bash
git clone https://github.com/yourusername/motivation-bot.git
```

Создать новую ветку для разработки:
```bash
git checkout -b new-feature
```
После внесения изменений сделайте коммит:
```bash
git commit -am "Добавлена новая фича"
```
Отправьте изменения в репозиторий:
```bash
git push origin new-feature
```


## Автор

👤 **SCaeR42@SpaceCoding**

* Сайт: [spacecoding.net](https://spacecoding.net/)
* Github: [@SCaeR42](https://github.com/SCaeR42)

## Покажите свою поддержку

Поставьте ⭐️, если этот проект вам помог!

## Лицензия

Авторское право (C) 2025 [spacecoding.net](https://spacecoding.net/)

Лицензия [MIT](https://choosealicense.com/licenses/mit/).
