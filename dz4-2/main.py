all_products = {'Весь склад': {}}
korzina = []

while True:
    action = input('Выберите действие: ')

    if action.lower() == 'добавить':
        product_name = input('Введите продукт: ')
        product_count = int(input('Количество: '))
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
                if all_products['Весь склад'][product_to_buy] == 0:
                    del all_products['Весь склад'][product_to_buy]
                print('Продукт добавлен в корзину!')
        else:
            print('Такого товара нет!')

    elif action.lower() == 'продукты':
        print(all_products)

    elif action.lower() == 'удалить':
        product_to_delete = input('Введите товар для удаления: ')
        product_count_delete = int(input('Введите количество для удаления: '))
        found = False  # Флаг для отслеживания наличия товара в корзине
        for item in korzina:
            if product_to_delete in item:
                if item[product_to_delete] >= product_count_delete:
                    item[product_to_delete] -= product_count_delete
                    if item[product_to_delete] == 0:
                        korzina.remove(item)
                    print(f'Удалено {product_count_delete} единиц товара {product_to_delete}')
                else:
                    print('В корзине нет такого количества товара для удаления')
                found = True
                break
        if not found:
            print('Товар для удаления не найден в корзине')

    else:
        print('Неизвестная операция')

