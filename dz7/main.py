# Домашнее задание. Повторение

# Переменные
# model = "Gentra"
# print(model)

# Списки, кортежи. Слайсинги. Методы списков.
# lis = [1, 2, "3", 4.50, ["Hello", "World!"]]
# print(lis)
# print(lis[4][0])
# print(lis[1:4])
# lis.append("The last element")
# print(lis)
# lis.insert(2,"Changed element")
# print(lis)
# lis.extend([8, 9, 10])
# print(lis)
# lis2=lis.copy()
# lis2.pop()
# print(lis2)
# lis2.pop(2)
# print(lis2)
# lis2.remove(8)
# print(lis2)
# lis2.clear()
# print(lis2)

# tup = ("One", "Two", "Three", "Four", 5, 6)
# print(tup)
# print(tup[::-1])


# Циклы
# list_exam = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'h', 'o', 'w', ' ', 'w', 'e', ' ', 'd', 'o']
# for i in list_exam:
#     print(i)

# for i in range(1,11):
#     print(i)

# list_1 = [1, 2, 3, 4, 5, 6]
# i = len(list_1)
# while i <= 6:
#     print("Элемент")
#     list_1.pop()


# list comprehension
# hello = ['H','e','l','l','o']
# hello2 = [i + ' ' for i in hello ]
# print(hello2)


# Словари
# dictionary = {"name": "Sasha", "age": 38, "hobbies": ["Рыбалка", "Футбол", "Охота"]}
# print(dictionary.values())
# print(dictionary.keys())
# print(dictionary.items())

# dictionary_2 = dict(model="Lexus", year=2023, mileage=0)
# dictionary_2["weight"] = 2500
# print(dictionary_2)

# dictionary_3 = dict(name="male", age=100, model="250", grade=1000)
# print(dictionary_3)
# dictionary_3.pop("name")
# print(dictionary_3)
#
# dictionary_4 = dictionary_3.copy()
# dictionary_4.clear()
# print(dictionary_4)
#
# key_dict = dictionary_3.get("model")
# print(key_dict)


# Сеты
# set_1 = ("Hello", "Hello", "Hello", "World", "World")
# set_2 = set(set_1)
# print(set_2)


# spis = dict(num1=1, num2=2, num3=3, num4=4)
# for i in spis.values():
#     print(i)

# spis2 = dict(name1="Mike", name2="Shinoda", name3="Who",name4="Ken")
# for i,m in spis2.items():
#     print(i, m)


# Функции
# def cheking():
#     word1 = input("Введите слово 'год' ")
#     word2 = input("Введите слово 'дракона' ")
#     print(word1+" "+word2)
# cheking()


# lambda функция
# num = int(input("Введите число: "))
# equite = lambda num: num**2
# print(equite(num))

# def step(*args):
#     return args
# print(step(1, 2, 3, 4, 5))


# Классы, атрибуты, методы

# class Human:
#     age = 29
#     weihgt = 85
#     height = 175
#     sex = "male"


# class Food:
#     def __init__(self, type, temperature, calories):
#         self.type = type
#         self.temperature = temperature
#         self.calories = calories
# dinner = Food("solid", "Hot", 540)
# print(dinner.temperature)


# class Technic:
#     def __init__(self, type, model):
#         self.type = type
#         self.model =   model
#
#     def start(self):
#         print("Запустился.")
#
#     def stop(self):
#         print("Завершил работу.")
#
#     def model_change(self, new_model):
#         self.model = new_model
#
# computer = Technic("Workstation", "HP")
# print(computer.model)
# computer.model_change("Dell")
# print(computer.model)
# computer.start()


# Наследование


# class Building:
#     def __init__(self, type, floors, square):
#         self.type = type
#         self.floors =  floors
#         self.square = square
#
# class Supermarket (Building):
#     def __init__(self, type, floors, square, parking):
#         super().__init__(type, floors, square)
#         self.parking =  parking


# Декораторы

# class Test:
#     @classmethod
#     def test_func(cls):
#         return "Вывод метода класса, минуя создание экземпляра этого класса."
# print(Test.test_func())


# Этот декоратор не особо понял, потому, что всё работет без него,
# если написать print(object_1.equil()) вместо print(object_1.equil)
# class Square:
#     def __init__(self, storona_a, storona_b):
#         self.storona_a = storona_a
#         self.storona_b = storona_b
#     @property
#     def equil(self):
#         return self.storona_a * self.storona_b
#
# object_1 = Square(2, 3)
# print(object_1.equil)
# object_1.storona_b = 5
# print(object_1.equil)


# Базы данных (базу не запускал)

# import sqlite3
# connection = sqlite3.connect("test.db")
# sql = connection.cursor()
# sql.execute("CREATE TABLE IF NOT EXISTS table1 (id INTEGER, name TEXT, comment TEXT);")
# sql.execute("INSERT INTO table1 (id, name, comment) VALUES (0, 'First', 'Like';")
# sql.execute("INSERT INTO table1 (id, name, comment) VALUES (1, 'Second', 'Like';")
#
# print( sql.execute("SELECT * FROM table1;").fetchall() )
#
# sql.execute("UPDATE table1 SET comment='Dislike' WHERE id=1;")
# sql.execute("DELETE FROM table1 WHERE comment='Dislike';")
#
# connection.commit()
