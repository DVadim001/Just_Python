spis = ['Pavel', 'Sasha', 'Ivan', 'Petya']
print(spis)
edited_name = input('Введите имя для редактирования: ')
# Получаем индекс удаляемого имени перед его удалением
index_to_replace = spis.index(edited_name)
spis.remove(edited_name)
new_name = input('Введите новое имя: ')
# Вставляем новое имя на запомненный индекс
spis.insert(index_to_replace, new_name)
print(spis)
