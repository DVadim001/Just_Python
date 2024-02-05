# Создание базы students на sqlite3

import sqlite3

connection = sqlite3.connect("mydatabase.db")
sql = connection.cursor()
# sql.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, age INTEGER, grade TEXT);")
# sql.execute("INSERT INTO students (id, name, age, grade) VALUES (0, 'Pavel', 25, 5);")
# sql.execute("INSERT INTO students (id, name, age, grade) VALUES (1, 'Masha', 29, 4);")
# sql.execute("INSERT INTO students (id, name, age, grade) VALUES (2, 'Jordan', 23, 3);")
# sql.execute("INSERT INTO students (id, name, age, grade) VALUES (3, 'Oleg', 31, 5);")
# sql.execute("INSERT INTO students (id, name, age, grade) VALUES (4, 'Dima', 27, 4);")

print(sql.execute("SELECT * FROM students;").fetchall())

connection.commit()


def get_student_by_name():
    name = input("Введите имя студента для просмотра его данных: ")
    sql = connection.cursor()
    print(sql.execute(f"SELECT name, age, grade FROM students WHERE name='{name}';").fetchone())
    print(sql.execute("SELECT * FROM students;").fetchall())
    connection.commit()


def update_student_by_name():
    name = input("Введите имя студента для изменения его оценки: ")
    grade = input("Введите его новую оценку: ")
    sql = connection.cursor()
    sql.execute(f"UPDATE students SET grade='{grade}' WHERE name='{name}';")
    print(sql.execute("SELECT * FROM students;").fetchall())
    connection.commit()


def delete_student():
    name = input("Введите имя студента для его удаления: ")
    sql = connection.cursor()
    sql.execute(f"DELETE FROM students WHERE name='{name}';")
    print(sql.execute("SELECT * FROM students;").fetchall())
    connection.commit()


# get_student_by_name()
# update_student_by_name()
# delete_student()
