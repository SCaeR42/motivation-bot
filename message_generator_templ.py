# Генерация сообщений с помощью шаблонов
import random
from datetime import datetime

# Мотивационные сообщения по времени суток
morning_messages = [
    "Доброе утро! Сегодня твой день для великих достижений.",
    "Начни утро с улыбки, и весь день будет успешным."
]

afternoon_messages = [
    "Полдень! Ты уже сделал значительный прогресс, продолжай в том же духе.",
    "Успех на подходе, не останавливайся!"
]

evening_messages = [
    "Вечер. Время подвести итоги дня. Ты сделал всё возможное, теперь отдыхай.",
    "Закат — это лишь начало нового дня для новых возможностей."
]

# Генерация сообщения в зависимости от времени суток
def generate_time_based_message():
    current_hour = datetime.now().hour
    
    if 6 <= current_hour < 12:
        return random.choice(morning_messages)
    elif 12 <= current_hour < 18:
        return random.choice(afternoon_messages)
    else:
        return random.choice(evening_messages)

# Пример использования
if __name__ == "__main__":
    print(generate_time_based_message())
