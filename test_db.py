import db

# Создаем пользователей с русскими именами
db.insert_user('Иван Иванов', 'ivan@example.com')
db.insert_user('Мария Смирнова', 'maria@example.com')

# Получаем user_id для пользователей
user_id_ivan = db.get_user_id('ivan@example.com')
user_id_maria = db.get_user_id('maria@example.com')

# Добавляем мероприятия для Ивана Иванова
db.insert_event('Мастер-класс по Python', 'Основы программирования на Python', '2024-05-01 10:00', 'Кабинет 101', user_id_ivan)
db.insert_event('Обучение Django', 'Создание сайтов с использованием Django', '2024-05-01 14:00', 'Кабинет 102', user_id_ivan)

# Попробуем добавить мероприятие с тем же временем для Ивана Иванова (должно быть отклонено)
db.insert_event('Мастер-класс по Python (дублирование)', 'Повтор мастер-класса по Python', '2024-05-01 10:00', 'Кабинет 103', user_id_ivan)

# Добавляем мероприятия для Марии Смирновой
db.insert_event('Семинар по Data Science', 'Введение в Data Science', '2024-06-01 09:00', 'Кабинет 201', user_id_maria)
db.insert_event('Лекция по машинному обучению', 'Основы машинного обучения', '2024-06-01 14:00', 'Кабинет 202', user_id_maria)

# Попробуем добавить мероприятие с тем же временем для Марии Смирновой (должно быть отклонено)
db.insert_event('Семинар по Data Science (дублирование)', 'Повтор семинара по Data Science', '2024-06-01 09:00', 'Кабинет 203', user_id_maria)

# Загрузим и выведем все мероприятия
events = db.load_events()
for event in events:
    print(f"Название: {event[1]}, Дата: {event[3]}, Место: {event[4]}")
