# School management:
# есть школа,
# в школе есть классы, их можно добавлять и удалять, удалять не-пустые классы нельзя,
# в классах есть ученики, их можно добавлять в классы, переводить из класса в класс, удалять и классов (из школы) ),
# школе есть учителя, их можно добавлять в классы, удалять из классов, заменять на нового,
# в учениках есть оценки (добавляются в ученики, удаляются из учеников, изменяются в учениках),
# учителя могут изменять оценки в учениках по запросу: какой учитель - какой ученик - какая оценка

school = []


# Действия с классами школы
# Добавляем класс в школу
def add_class():
    pass


# Удаляем класс из школы
def delede_class():
    pass


# Действия с учениками
# Добавляем ученика в класс
def add_pupil():
    pass


# Меняем ученику класс
def move_pupil():
    pass


# Удаляем ученика из класса
def delete_pupil():
    pass


# Действия с учителями
# Добавляем учетеля в класс
def add_teacher():
    pass


# Заменяем учителя в классе на нового
def move_teacher():
    pass


# Удаляем учетеля из класса
def delete_teacher():
    pass


# Действия с оценками
# Добавление оценки учителем в ученика (своего класса)
def add_mark():
    pass


# Bpvtytybt оценки учителем в ученикt (своего класса)
def change_mark():
    pass


pupils = {'Ученики': {}}
open_classrooms = [i for i in range(1, 21)]
closed_classrooms = []


def register(name, classroom):
    if pupils[name] not in pupils['Ученики']:
        pupils['Ученики'][name] = classroom
        open_classrooms.remove(name)
        closed_classrooms.append(name)
        print(f'Ученик добавлен в {pupils['Ученики']}\n')
    else:
        print(f'Такой ученик уже существует. Он учится в {pupils['Ученики'][name]} классе.')


def delete(name):
    closed_classrooms.remove(pupils[name])
    open_classrooms.append(pupils[name])


def closed_rooms():
    return closed_classrooms


action = input('Выберите действие: ')

if action.lower() == 'добавить':
    pupils_name = input('Введите имя: ')
    print(open_classrooms)
    pupils_room = input('Выберите класс: ')
    register(pupils_name, pupils_room)


elif action.lower() == 'убрать':
    pupils_name = input('Введите имя: ')
    if pupils_name in pupils:
        delete(pupils_name)
    else:
        print('Нет такого ученика.')

elif action.lower == 'занятые':
    print(closed_rooms())
else:
    print('Неизвестная операция.')


# sum = lambda chislo1,chislo2: chislo1+chislo2
# chislo1 = int(input('Введите первое число: '))
# chislo2 = int(input('Введите второе число: '))
#
# print(sum(chislo1,chislo2))
