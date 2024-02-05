word = input('Введите слово: ')


if word[::-1] == word:
    print('Палиндром')
else:
    print('Не палиндром')

word2 = word[::-1]
