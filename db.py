import sqlite3


# Модуль для работы с базой данных

def create_db():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    # Создаем таблицу для пользователей с уникальным email
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE)''')

    # Создаем таблицу для мероприятий с внешним ключом user_id, который ссылается на id из таблицы users
    c.execute('''CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    date TEXT,
                    location TEXT,
                    user_id INTEGER,
                    FOREIGN KEY(user_id) REFERENCES users(id))''')

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()


# Вставка данных
def insert_user(name, email):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    # Проверяем, есть ли пользователь с таким email
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_user = c.fetchone()

    if not existing_user:
        # Если пользователь не найден, добавляем нового
        c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    else:
        print(f"Пользователь с email {email} уже существует.")

    conn.close()


def insert_event(title, description, date, location, user_id):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    # Добавляем новое мероприятие с указанием user_id
    c.execute("INSERT INTO events (title, description, date, location, user_id) VALUES (?, ?, ?, ?, ?)",
              (title, description, date, location, user_id))
    conn.commit()
    conn.close()


# Загрузка мероприятий
def load_events():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    # Запрос с сортировкой по дате (по возрастанию)
    c.execute("SELECT * FROM events ORDER BY date ASC")
    events = c.fetchall()

    conn.close()
    return events


# Получение user_id по email
def get_user_id(email):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()

    c.execute("SELECT id FROM users WHERE email = ?", (email,))
    user_id = c.fetchone()

    conn.close()
    return user_id[0] if user_id else None
