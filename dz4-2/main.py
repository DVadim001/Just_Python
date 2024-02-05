all_products = {'Весь склад': {}}
korzina = []

while True:
    action = input('Выберите действие')

    if action.lower() == 'добавить':
        product_name = input('Введите продукт: ')
        product_count = int(input('Количество:'))
        all_products['Весь склад'][product_name] = product_count
        print(f'Продукт {product_name} успешно добавлен в количестве {product_count}')

    elif action.lower() == 'корзина':
        product_to_buy = input('Введите название товара: ')
        if product_to_buy in all_products['Весь склад'].keys():
            product_count = int(input('Введите количество: '))
            if product_count > all_products['Весь склад'][product_to_buy]:
                print('На складе нет такого количества')
            else:
                korzina.append({product_to_buy: product_count})
                all_products['Весь склад'][product_to_buy] -= product_count
                print('Продукт добавлен в корзину!')
        else:
            print('Такого товара нет!')

    elif action.lower() == 'продукты':
        print(all_products)

    elif action.lower() == 'удалить':
        product_to_delete = input('Введите товар для удаления: ')
        product_count_delete = int(input('Введите количество для удаления: '))
        if product_to_delete in korzina[0].keys():
            korzina.pop(product_to_delete)
    else:
        print('Неизвестная операция')
