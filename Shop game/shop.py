class Product:
    def __init__(self, name, purchase_price, sell_price, quantity=0, stak=False):
        self.name = name
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.stak = stak

    def str(self):
        return f"{self.name}: {self.quantity} шт. (покупка: {self.purchase_price}, продажа: {self.sell_price})"

    def stak_product(self):
        if self.stak:
            quanity = 1


class Player:
    def __init__(self, name, initial_balance=1000, max_storage=50):
        self.name = name
        self.balance = initial_balance
        self.inventory = []  # Список объектов Product
        self.max_storage = max_storage

    def get_total_items(self):
        """Получить общее количество товаров на складе"""
        return sum(product.quantity for product in self.inventory)

    def get_free_space(self):
        """Получить свободное место на складе"""
        return self.max_storage - self.get_total_items()

    def find_product(self, product_name):
        """Найти товар в инвентаре по имени"""
        for product in self.inventory:
            if product.name == product_name:
                return product
        return None

    def buy(self, product_name, quantity_to_buy):
        """
        Купить товар

        Проверки:
        1. Хватает ли денег
        2. Хватает ли места на складе
        """
        product = self.find_product(product_name)

        if product is None:
            print(f"Товар '{product_name}' не найден в ассортименте")
            return False

        total_cost = product.purchase_price * quantity_to_buy
        required_space = quantity_to_buy

        # Проверка наличия денег
        if self.balance < total_cost:
            print(f"Недостаточно средств! Нужно: {total_cost}, есть: {self.balance}")
            return False

        # Проверка свободного места на складе
        if self.get_free_space() < required_space:
            print(f"Недостаточно места на складе! Нужно: {required_space}, свободно: {self.get_free_space()}")
            return False

        # Совершение покупки
        self.balance -= total_cost
        product.quantity += quantity_to_buy
        print(f"Куплено {quantity_to_buy} шт. товара '{product_name}' за {total_cost}")
        print(f"Баланс: {self.balance}, на складе: {product.quantity} шт.")
        return True

    def sell(self, product_name, quantity_to_sell):
        """
        Продать товар

        Проверки:
        1. Есть ли товар в инвентаре
        2. Достаточно ли товара для продажи
        """
        product = self.find_product(product_name)

        if product is None:
            print(f"Товар '{product_name}' не найден в инвентаре")
            return False

        # Проверка наличия достаточного количества товара
        if product.quantity < quantity_to_sell:
            print(f"Недостаточно товара! Есть: {product.quantity}, нужно продать: {quantity_to_sell}")
            return False

        # Проверка, что количество не отрицательное
        if quantity_to_sell <= 0:
            print("Количество для продажи должно быть положительным!")
            return False

        # Совершение продажи
        total_income = product.sell_price * quantity_to_sell
        self.balance += total_income
        product.quantity -= quantity_to_sell

        print(f"Продано {quantity_to_sell} шт. товара '{product_name}' за {total_income}")
        print(f"Баланс: {self.balance}, осталось на складе: {product.quantity} шт.")

        # Удаляем товар из инвентаря, если количество стало 0
        if product.quantity == 0:
            self.inventory.remove(product)
            print(f"Товар '{product_name}' удален из инвентаря (закончился)")

        return True

    def add_product_to_market(self, product):
        """Добавить товар в ассортимент (в инвентарь)"""
        self.inventory.append(product)
        print(f"Товар '{product.name}' добавлен в ассортимент")

    def show_inventory(self):
        """Показать инвентарь игрока"""
        print(f"\n=== ИНВЕНТАРЬ ИГРОКА {self.name} ===")
        print(f"Баланс: {self.balance}")
        print(f"Склад: {self.get_total_items()}/{self.max_storage} (свободно: {self.get_free_space()})")

        if not self.inventory:
            print("Инвентарь пуст")
            return

        for i, product in enumerate(self.inventory, 1):
            print(f"{i}. {[product.name]}")
        print()


# Демонстрация работы программы
def main():
    # Создаем игрока
    player = Player("Алекс", initial_balance=1500, max_storage=30)

    # Создаем товары
    apple = Product("Яблоки", purchase_price=10, sell_price=15, quantity=0)
    bread = Product("Хлеб", purchase_price=20, sell_price=30, quantity=0)
    milk = Product("Молоко", purchase_price=25, sell_price=35, quantity=0)

    # Добавляем товары в ассортимент
    player.add_product_to_market(apple)
    player.add_product_to_market(bread)
    player.add_product_to_market(milk)

    # Показываем начальное состояние
    player.show_inventory()

    # Тестовые покупки
    print("=== ПОКУПКИ ===")
    player.buy("Яблоки", 5)  # Успешная покупка
    player.buy("Хлеб", 10)  # Успешная покупка
    player.buy("Молоко", 20)  # Должно не хватить места (5+10+20 = 35 > 30)

    player.show_inventory()

    # Продажи
    print("=== ПРОДАЖИ ===")
    player.sell("Яблоки", 3)  # Успешная продажа
    player.sell("Хлеб", 15)  # Должно не хватить товара (есть только 10)
    player.sell("Хлеб", 5)  # Успешная продажа

    player.show_inventory()

    # Пробуем купить снова (теперь есть место)
    print("=== ЕЩЕ ПОКУПКИ ===")
    player.buy("Молоко", 10)  # Теперь должно хватить места

    player.show_inventory()

    # Продаем весь товар
    print("=== ПРОДАЖА ВСЕГО ===")
    player.sell("Яблоки", 2)  # Продаем оставшиеся яблоки (должны удалиться)
    player.sell("Хлеб", 5)  # Продаем оставшийся хлеб (должен удалиться)
    player.sell("Молоко", 10)  # Продаем все молоко (должно удалиться)

    player.show_inventory()

