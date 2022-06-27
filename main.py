from classes.request import Request
from classes.shop import Shop
from classes.store import Store


def main():
    while True:
        user_input = input("Введите запрос по типу\n"
                           "'Доставить 3 печеньки из склад в магазин'\n")

        # Проверка на стоп
        if user_input.lower() == "стоп":
            break

        # Проверка на правильность введеных данных
        if len((user_input.split(" "))) != 7:
            print("Введите корректную строку")
            continue

        request = Request(user_input)

        # Проверка на валидность введеных данных
        if request.amount <= 0:
            print("Количество не может быть 0 или меньше 0")
            continue

        # Определение пунктов назначений
        place_from = store if request.from_ == "склад" else shop
        place_to = store if request.to_ == "склад" else shop

        # Проверка условий для пункта 'ИЗ'

        # Проверка на наличие
        if request.product in place_from.items:
            print(f"Нужный товар есть в пункте {place_from}")
        else:
            print(f"Нужного товара нет в пункте {place_from}")
            continue

        # Проверка на необходимое количество
        if (place_from.items[request.product] - request.amount) >= 0:
            print(f"Нужное количество есть в пункте {place_from}")
        else:
            print(f"Нужного количества нет в пункте {place_from}")
            continue

        # Проверка условий для пункта 'В'

        # Проверка на свободное место
        if place_to.capacity - request.amount >= 0:
            print(f"В пункте {place_to} достаточно места")
        else:
            print(f"В пункте {place_to} недостаточно места, не хватает {request.amount - place_to.capacity}")
            continue

        # Работа Курьера
        print(f"Курьер забрал {request.amount} {request.product} со {place_from}")
        print(f"Курьер везет {request.amount} {request.product} со {place_from} в {place_to}")
        place_from.remove(request.product, request.amount)
        place_to.add(request.product, request.amount)
        print(f"Курьер доставил 3 собачки в магазин")
        print("="*30)

        # Информация о пунтках
        print(f"В пункте {place_from} хранится:")
        for item, amount in place_from.items.items():
            print(f"{amount} {item}")

        print("="*30)
        print(f"В пунтке {place_to} хранится:")
        for item, amount in place_to.items.items():
            print(f"{amount} {item}")
        print("=" * 30)


if __name__=="__main__":

    # Создание классов
    store = Store()
    shop = Shop()

    # Добавление товаров
    store.add('яйцо', 10)
    store.add('огурец', 5)
    store.add('печеньки', 20)
    store.add('молоко', 15)

    shop.add('печеньки', 5)

    main()
