import psycopg2
from psycopg2 import sql

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="postgres"
)
# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()


def register_user(login, first_name, last_name, account, is_active):
    # SQL-запрос для вставки данных пользователя
    query = sql.SQL("""
        INSERT INTO my_table (login, first_name, last_name, account, is_active)
        VALUES (login, first_name, last_name, account, is_active)
    """)
    try:
        # Выполнение запроса с передачей значений
        cursor.execute(query)
        # Фиксация изменений
        conn.commit()
        print("Пользователь " + login + " успешно зарегистрирован!")
    except psycopg2.Error as e:
        # Обработка ошибки при выполнении запроса
        print("Ошибка при регистрации пользователя: " + login, e)
    finally:
        # Закрытие курсора и соединения с базой данных
        cursor.close()
        conn.close()
