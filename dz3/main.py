spis = ['Pavel', 'Sasha', 'Ivan', 'Petya']
print(spis)
edited_name = input('Введите имя для редактирования: ')
new_name = input('Введите новое имя: ')

index_element = spis.index(edited_name)
spis[index_element] = new_name
print(spis)
