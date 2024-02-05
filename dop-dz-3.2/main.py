summa_zakaza = float(input('Введите сумму заказа: '))

# налог 12%
nalog = summa_zakaza / 100 * 12

# чаевые  18% от суммы заказа без налога
chaevie = summa_zakaza / 100 * 18

obschaya_summa = summa_zakaza + nalog + chaevie

# на выходе отдельно сумма налога, сумму чаевых и общий итог
print(f'Сумма Вашего заказа составляет: {round(obschaya_summa, 2)}\nЧаевые: {round(chaevie, 2)}\n'
      f'Отдельный налог: {round(nalog, 2)}')
