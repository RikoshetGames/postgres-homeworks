"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="645595")


# Создание курсора
cur = conn.cursor()

try:
    # Загрузка данных из файла "employees.csv" в таблицу employees
    with open("north_data/employees_data.csv", "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                f'INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)'
                f'VALUES (%s, %s, %s, %s, %s, %s)',
                (row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))

    # Загрузка данных из файла "customers.csv" в таблицу customers
    with open("north_data/customers_data.csv", "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                f'INSERT INTO customers (customer_id, company_name, contact_name)'
                f'VALUES (%s, %s, %s)',
                (row["customer_id"], row["company_name"], row["contact_name"]))

    # Загрузка данных из файла "orders.csv" в таблицу orders
    with open("north_data/orders_data.csv", "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                f'INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)'
                f'VALUES (%s, %s, %s, %s, %s)',
                (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))


    # Сохранение изменений
    conn.commit()
finally:
    # Закрытие курсора и соединения
    cur.close()
    conn.close()