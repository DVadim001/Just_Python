list1 = 'theword'
name = [i for i in list1]
print(name)

list2 = ['a', 'b', 'c', 'e', 'f', 'g']
name = ['the '+i for i in list2]
print(name)

list3 = [i for i in range(1, 21)]
print(list)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = [i for i in list4 if i % 2 == 0]
print(num)

list5 = ['Pavel', 'Ivan', 'Timur', 'Oleg', 'Vanya', 'Olga']
name = [i for i in list5 if 'a' in i or 'o' in i]
print(name)

numbers = [i for i in range(1, 21)]
num = [i*2 for i in numbers]
print(num)

names = ['Pavel', 'Roma', 'Ivan', 'Vasya', 'Elena', 'Timur']
word = [i[0] for i in names]
print(word)
