# names = ['Loki', 'Spider-man']
# names.insert(0, 'Thor')
# print(names)
#
# names = ['Loki', 'Spider-man']
# names.extend(['Thor', 0, 23, 'Tanos'])
# print(names)

# names = [1, 2, 3, 4, 5]
# names.clear()
# print(names)
#
# names = [1, 2, 3, 4, 5]
# names.pop()
# print(names)
#
# names = [1, 2, 3, 4, 5]
# names.pop(3)
# print(names)
#
# names = [1, 2, 3, 4, 5]
# names.remove(3)
# print(names)
#
# name = ['Pavel', 'Python', 'TgBot', 'Django']
# print(name)
# name[0] = 'Tehnikum'
# print(name)

# name = ['Pavel', 'Python', 'TgBot', 'Django']
# name_index = name.index('Pavel')
# print(name_index)

# toys = ('Мишка', 'Мячик', 'Робот', 'Машинка')
# toys2 = list(toys)
# print(type(toys2))

# spis = []
# spis.append(input('Введите имя: '))
# print(spis)

# names = ['Pavel','Sasha','Ivan','Petya']
# for i in names:
#     print(i + ' крутой')

# my_list = (6, 4, '2')
# for t in my_list:
#     print(t+2)

# my_tuple = (6, 4, '2')
# for i in range(1, 100):
#     print(f'{my_tuple}')

# names = ['Pavel','Sasha','Ivan','Petya']
# for i in range(1, 20):
#     if 'Pavel' in names:
#         print('Pavel есть в списке')
#     else:
#         print('Нет такого')

# words = ['adopt', 'bake', 'beam', 'confide', 'grill', 'wave']
# past_tense = []
# for word in words:
#     if word[-1] != 'e':
#         past_tense.append(word+'ed')
#     else:
#         past_tense.append(word + 'd')
#     print(past_tense)

# names = ['Pavel','Sasha','Ivan']
# while True:
#     new = input('Добавьте нового пользователя: ')
#     names.append(new)
#     print(names)


# spis_name = []
# spis_numb = []
# spis_usl = []
#
# while True:
#     new_data = input('Введите данные: ')
#     if 'Номер ' in new_data:
#         new_numb = input('Добавьте новый номер: ')
#         spis_numb.append(new_numb)
#
#     elif 'Имя' in new_data:
#         new_name = input('Добавьте новое имя: ')
#         spis_name.append(new_name)
#     else:
#         new_usl = input('Добавьте новую услугу: ')
#         spis_usl.append(new_usl)
#
#     print(spis_name, spis_numb, spis_usl)


# nums = [i for i in range(1,21)]
# print (nums)

# text = input('Введите что-то: ')
# if text.title() == 'Привет':
#     print('Привет')
# print(text.title())


# my_list = [1,2,4.5]
# my = [i+2 for i in my_list]
# print(my)


# my = ['2','33','Jordan','Pavel']
# my2 = [i + '2' for i in my]
# print(my2[1:3])


# names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
# answer = [i[0] for i in names]
# print(answer)


# nums = [i for i in range(1,21)]
# nums_chetn = [i for i in nums if i%2  == 0]
#
# print((nums))
# print((nums_chetn))


# username = []
# while True:
#     name = input('Введите имя: ')
#     if name in username:
#         print(f' {name} уже существует')
#     else:
#         username.append(name)
#         print(f' {name} добавлен')
#     print(username)


# Словари


# x = {'name':'Pasha', 'job':'TGbot'}
# print(x['name'],x['job'])


# data = {'name': ['Jordan', 'Pavel'],
#         'age': (12,21),
#         'job': 'programmers'}
# p = data['name'][0]
# print(p)
# print(data['name'][0], data['job'][-1])


# instructor = {'name': 'Jordan', 'age': 21,'job': 'programmer'}
# print(instructor.keys())
# print(instructor.values())
# print(instructor.items())


# instructor = {'name': 'Jordan', 'age': 21,'job': 'programmer'}
# if 'name' in instructor:
#     print('Da')
# else:
#     print('Net')


# users = {}
# users['name'] = 'Jordan'
# print(users)
# print(users['name'])


# my_dict = {'name': 'Jordan'}
# my_dict['name'] = 'Pasha'
# print(my_dict)


# instructor = {'name': 'Jordan', 'age': 21,'job': 'programmer'}
# instructor.pop('job')
# print(instructor)
# instructor.popitem()
# print(instructor)
# instructor.clear()
# print(instructor)


# instructor = {'name': 'Jordan', 'age': 21,'job': ['programmer', 'freelance']}
# instructor['job'].pop(1)
# print(instructor)


# my = dict(name='Jordan', job='Developer', age=23)
# my2 = my.get('name')
# print(my2)


# my = ['2','33','33',2,'TG']
# my2 = set(my)
# print(my2)


# instructor = {'name': 'Jordan', 'age': 21,'job': 'programmer'}
# for v in instructor.keys():
#     print(v)

# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# for v in instructor.values():
#     print(v)


# instructor = {'name': 'Jordan', 'age': 21,'job': 'programmer'}
# for k,v in instructor.items():
#     print(k,v)


# prazd = {'Навруз': '21 марта', 'Новый год': '1 декабря'}
# day = input('Какой праздник ')
# print(prazd.get(day))


# Функции

# def create_list():
#     my_list = []
#     print((my_list))
#
# create_list()
#
# def say_hello():
#     print('Hello World')
#
# say_hello()
#
#
# def calc():
#     print(3+5)
#
# calc()


# def craete_list():
#     my_list = []
#     return my_list

# craete_list()
# print(craete_list())


# import requests
# link ='https://www.httpbin.org/forms/post'
# print(requests.get(link).text)


# import requests
# link ='https://www.httpbin.org/post'
#
#
# data = {
# "comments": "make it good",
#     "custemail": "vvd-ghost@mail.ru",
#     "custname": "vadim",
#     "custtel": "2676301",
#     "delivery": "12:00",
#     "size": "medium",
#     "topping": [
#       "bacon",
#       "mushroom"
#     ]
# }
# print(requests.post(link).status_code)


# Функции


# a = lambda x: 2*x+5
# print(a(3))


# b = lambda y,u: y+u
# print(b(2,3))

# x = lambda e:e
# print(x(9))


# p = lambda a: a*4
# storona = int(input('Введите сторону квадрата: '))
# print(p(storona))


# def spam(a):
#     print(a+6)
#
# spam(5)


# def spam(a,b,c=7):
#     print(a+b+c)
#
# spam(3,5, 8)


# numbers = [i for i in range(1,21)]
# chet = list(filter(lambda x: (x%2==0), numbers))
# print(chet)


# numbers1 = [i for i in range(1,41)]
# squares = list(map(lambda e: e**2, numbers1))
# print(squares)


# def sum(a,b):
#     print(a+b)
#
# sum(3,5)


# def spam(*args):
#     return args
#
# print(spam(1,2,3,'Hello'))


# def spam(*args):
#     for a in args:
#         print(a)
#
# spam(1,2,3,1,2,3,'4','Hello')


# def spam(**kwargs):
#     return kwargs
#
# print(spam(name = 'my1', age = 23))


# def spam(**kwargs):
#     for k,v in kwargs.items():
#         print (k,v)
#
# spam(name='my1', age=23)


# while True:
#     def chisla(*args):
#         num = int(input('Введите число: '))
#         if num % 2 == 0:
#             print('Чётное')
#             return num
#         elif num % 2 ==1:
#             print('Нечётное')
#             return num
#
#     chisla()


# Классы и методы


# class User:
#     name = 'Jordan'
#
# user1 = User()
# print(user1.name)


# class Person:
#     name = 'Jordan'
#     age = 23
#     job = 'programmer'
#
# class Car:
#     type = 'Bugatti'
#     color = 'white'
#     max_speed = 300


# class Car:
#     def __init__ (self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#
# chevrolet = Car(model='Gentra', color='Black', year=2023)
# print(chevrolet.year)


# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#
# com1 = Comment(username='One', text='Message', likes='yes')
# print(com1.username, com1.text, com1.likes)


# class Car:
#     def __init__ (self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# gentra = Car(model='Ravon', color='Black', year=2023)
#
# gentra.change_color('White')
#
# print(gentra.color)
#
# print(gentra.year)
#
# gentra.stop()


# class User:
#     def __init__(self, name, mail, age, number):
#         self.name = name
#         self.mail = mail
#         self.age = age
#         self.number = number
#
#     def change_username(self,new_name):
#         self.name = new_name
#
#     def change_number(self, new_number):
#         self.number = new_number
#
#     def change_mail(self, new_mail):
#         self.mail = new_mail


# clients = {}
# opened_rooms = [i for i in range(1,41)]
# closed_rooms = []
#
# def register(name, room):
#     clients[name] = room
#     opened_rooms.remove(room)
#     closed_rooms.append(room)
#
# def delete(name):
#     closed_rooms.remove(clients[name])
#     opened_rooms.append(clients[name])
#     clients.pop(name)
#
# def show_rooms():
#     return closed_rooms
#
# while True:
#     action = input('Выберите действие: ')
#     if action.upper == 'РЕГИСТРАЦИЯ':
#         client_name = input('Введите имя: ')
#         print(opened_rooms)
#         client_room = int(input('Выберите номер: '))
#         if client_room in opened_rooms:
#             register(client_name, client_room)
#             print('Вы зарегистрировались!')
#             print(clients)
#         else:
#             print('Такого номера нет или он занят!')
#
#     elif action.upper() == 'ВЫСЕЛИТЬСЯ':
#         client_name = input('Введите имя: ')
#         if client_name in clients:
#             delete(client_name)
#             print('Приходите ещё!')
#             print(clients)
#         else:
#             print('Вас нет в базе.')
#
#     elif action.upper() == 'СПИСОК':
#         print(show_rooms())
#
#     else:
#         print('Неизвестная операция')


# Наследование и концепция ООП


# def x(values):
#     values[0] = 1
# v=[1,2,3,4]
# x(v)
# print(v)


# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Horse(Animal):
#     pass
#
#
# Horse1 = Horse()
# Horse1.make_sound('text')


# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.calor = color
#         self.year = year
#
#
# class SuperCar:
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor


# class MyClass:
#     def __init__(self,value):
#         self.value = value
#
#     @classmethod
#     def multiply(cls,value):
#         return value**2
#
# print(MyClass.multiply(4))


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle(4,5)
# print(rectangle.area)
#
# rectangle.width = 6
# print(rectangle.area)


# class Worker:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#
# class HR(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#
#     def view_position(self,worker_name):
#         return  worker_name.position
#
#
# jordan = Worker('Jordan','middle')
# pavel = HR('Pavel', 'HR')
#
# print(pavel.view_position(jordan))


# class Player:
#     def __init__(self,speed,power,accuracy,stamina):
#         self.speed = speed
#         self.power = power
#         self.accuracy = accuracy
#         self.stamina = stamina
#
# #нападающий
# class Striker(Player):
#     def __init__(self, speed, power, accuracy, stamina):
#         super().__init__(self, speed, power, accuracy, stamina)
#
#     def goal(self):
#         return 'Забил гол'
#
# #защитник
# class Defender(Player):
#     def __init__(self, speed, power, accuracy, stamina):
#         super().__init__(self, speed, power, accuracy, stamina)
#
#     def give_pass(self):
#         return 'Дал пас'
#
# #полузащитник
# class Midfielder(Player):
#     def __init__(self, speed, power, accuracy, stamina):
#         super().__init__(self, speed, power, accuracy, stamina)
#
#     def defend(self):
#         return 'Отразил удар'
#
# #вратарь
# class Goalkeeper(Player):
#     def __init__(self, speed, power, accuracy, stamina):
#         super().__init__(self, speed, power, accuracy, stamina)
#
#     def save(self):
#         return 'Поймал мяч'


# class BankAccaunt:
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, sum_dep):
#         self.balance += sum_dep
#
#     def cash(self, sum_cash):
#         self.balance -= sum_cash
#
#     def my_balance(self):
#         return self.balance
#
#
# client_name = input('Введите своё имя: ')
# client1 = BankAccaunt(name=client_name)
#
# while True:
#     action = input('Выберите действие: ')
#
#     if action.lower() == 'депозит':
#         sum = float(input('Сумма депозита: '))
#         client1.deposit(sum)
#         print('Операция успешна.')
#
#     elif action.lower == 'снять':
#         sum = float(input('Сумма для снятия: '))
#         if sum <= client1.balance:
#             client1.cash(sum)
#             print('Операция успешна.')
#         else:
#             print('Недостаточно средств.')
#
#     elif action.lower() == 'баланс':
#         print(client1.my_balance())
#
#     else:
#         print('Неизвестная операция.')


# Базы данных


# import sqlite3
# # Подключение к базе данных
# connection = sqlite3.connect('cars.db')
#
# # Pythin + SQL
# sql = connection.cursor() # писать в питоне на яз sql
#
# # Создание таблицы
# sql.execute('CREATE TABLE car '
#             '(model TEXT, color TEXT, year INTEGER, mileage REAL);')
#
# # сохраняем данные с помощью commit() метода у объекта connection


# Импортируем язык SQL
# import sqlite3
# # Подключение к БД
# conn = sqlite3.connect('my_users.db')
#
# #Python + SQL
# sql = conn.cursor()
#
# # Создание таблицы
# sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')
#
# # Добавляем данные в таблицу
# # sql.execute('INSERT INTO users (user_id, username) VALUES (0, "pav_ok");')
# # sql.execute('INSERT INTO users (user_id, username) VALUES (1, "lalala");')
# # sql.execute('INSERT INTO users (user_id, username) VALUES (2, "keeny");')
#
# #Вывод данных
# print(sql.execute('SELECT user_id, username FROM users;').fetchall() )
#
# #Вывод данных с условием
# # id = input('Введите id, чтобы узнать данные: ')
# # print(sql.execute(f'SELECT * FROM users WHERE user_id  = {id};').fetchone() )
#
# # Удаление из таблицы
# sql.execute('DELETE FROM users WHERE user_id = 0;')
#
#
# # Обновление данных в таблице
# sql.execute('UPDATE users SET username = "lolololo" WHERE user_id=1;')
#
# print(sql.execute('SELECT user_id, username FROM users;').fetchall())
#
# #закрепляем изменения (или после каждого дапроса, или в конце всех запросов)
# conn.commit()


# Телеграм боты (см. проект TelegramBot)
