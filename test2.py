class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):

        self.items[item_name] = price
        print(f'Товар {item_name} добавлен с ценой {price}.')

    def remove_item(self, item_name):

        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар {item_name} удален.')
        else:
            print(f'Товар {item_name} не найден в ассортименте.')

    def get_price(self, item_name):

        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):

        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена товара {item_name} обновлена до {new_price}.')
        else:
            print(f'Товар {item_name} не найден в ассортименте.')


store1 = Store("Магазин Ягодка", "ул. Ленина, 10")
store2 = Store("Магазин Фрукты", "ул. Пушкина, 15")
store3 = Store("Магазин Мечта", "ул. Чехова, 20")

# Добавление товаров в магазины
store1.add_item("яблоки", 100)
store1.add_item("бананы", 200)

store2.add_item("апельсины", 150)
store2.add_item("груши", 250)

store3.add_item("виноград", 300)
store3.add_item("киви", 400)

# Тестирование методов на одном из магазинов
print("\nТестирование методов для Магазина Ягодка:")
store1.add_item("персики", 350)
store1.update_price("яблоки", 120)
print(f"Цена яблок: {store1.get_price('яблоки')}")
store1.remove_item("бананы")
print(f"Цена бананов: {store1.get_price('бананы')}")
store1.remove_item("ананасы")
store1.update_price("ананасы", 500)