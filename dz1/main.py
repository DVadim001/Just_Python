
kamen = 'камень'
nojnic = 'ножницы'
bumag = 'бумага'

play1 = str(input('Первый игрок выбирает (камень, ножницы, бумага): '))
play2 = str(input('Второй игрок выбирает (камень, ножницы, бумага): '))

if play1 == kamen and play2 == kamen or play1 == nojnic and play2 == nojnic or play1 == bumag and play2 == bumag:
    print('ничья')
elif play1 == kamen and play2 == nojnic or play1 == nojnic and play2 == bumag or play1 == bumag and play2 == kamen:
    print('Победил первый игрок')
elif play2 == kamen and play1 == nojnic or play2 == nojnic and play1 == bumag or play2 == bumag and play1 == kamen:
    print('Победил второй игрок')
else:
    print('Введено неправильное значение')
