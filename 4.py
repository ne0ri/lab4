import os
import csv
from typing import Iterator, List


class Order:
    """Класс, описывающий один заказ."""
    def __init__(self, number: int, dish: str, order_time: str, cook_time: str, review: str):
        self.number = number
        self.dish = dish
        self.order_time = order_time
        self.cook_time = cook_time
        self.review = review

    def __repr__(self):
        return (f"{self.number:>3} | {self.dish:<20} | {self.order_time:<8} | "
                f"{self.cook_time:>5} мин | {self.review}")


class OrderManager:
    """Класс для управления коллекцией заказов."""
    FILE_PATH = "data.csv"
    FIELDNAMES = ["№", "Наименование блюда", "Время размещения заказа", "Время приготовления", "Отзыв"]

    def __init__(self):
        self.orders: List[Order] = []

    def load_orders(self) -> None:
        """Загружает заказы из CSV-файла."""
        if not os.path.exists(self.FILE_PATH):
            self.create_demo_orders()
        with open(self.FILE_PATH, "r", encoding="utf-8", newline='') as f:
            reader = csv.DictReader(f)
            self.orders = [
                Order(
                    number=int(row["№"]),
                    dish=row["Наименование блюда"],
                    order_time=row["Время размещения заказа"],
                    cook_time=row["Время приготовления"],
                    review=row["Отзыв"]
                )
                for row in reader
            ]

    def save_orders(self) -> None:
        """Сохраняет заказы в CSV-файл."""
        with open(self.FILE_PATH, "w", encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            for order in self.orders:
                writer.writerow({
                    "№": order.number,
                    "Наименование блюда": order.dish,
                    "Время размещения заказа": order.order_time,
                    "Время приготовления": order.cook_time,
                    "Отзыв": order.review
                })
        print("Данные сохранены в файл.")

    def create_demo_orders(self) -> None:
        """Создаёт демонстрационные заказы и сохраняет их."""
        demo_data = [
            (1, "Цезарь с курицей", "12:15", "15", "Очень вкусно, спасибо!"),
            (2, "Борщ", "13:00", "20", "Нормально, но хлеба мало"),
            (3, "Паста карбонара", "14:30", "12", "Отлично, как в Италии!"),
            (4, "Греческий салат", "15:45", "10", "Свежо и полезно"),
            (5, "Стейк рибай", "18:20", "25", "Средне, ожидал большего"),
            (6, "Лазанья", "19:10", "30", "Вкусно, но долго ждал"),
            (7, "Суп-пюре из тыквы", "12:05", "12", "Неожиданно вкусно"),
            (8, "Куриные крылышки", "20:00", "18", "Острые, но вкусные"),
            (9, "Чизкейк", "21:15", "5", "Лучший десерт!"),
            (10, "Морс клюквенный", "16:40", "3", "Освежает"),
        ]
        self.orders = [Order(num, dish, o_time, c_time, rev) for num, dish, o_time, c_time, rev in demo_data]
        self.save_orders()

    def add_order(self) -> None:
        """Добавляет новый заказ с консоли."""
        new_id = len(self.orders) + 1
        dish = input("Введите наименование блюда: ")
        order_time = input("Введите время размещения заказа (чч:мм): ")
        cook_time = input("Введите время приготовления (минуты): ")
        review = input("Введите отзыв: ")
        self.orders.append(Order(new_id, dish, order_time, cook_time, review))
        self.save_orders()

    # --- Генераторы ---
    def iter_orders(self) -> Iterator[Order]:
        """Генератор, последовательно выдающий все заказы."""
        for order in self.orders:
            yield order

    def filter_by_keyword_generator(self, keyword: str) -> Iterator[Order]:
        """Генератор заказов, в отзыве которых содержится ключевое слово (без учёта регистра)."""
        kw = keyword.lower()
        for order in self.orders:
            if kw in order.review.lower():
                yield order

    # Обычные сортировки (возвращают список, но можно было бы и генератор с sorted)
    def sort_by_dish(self) -> List[Order]:
        return sorted(self.orders, key=lambda o: o.dish)

    def sort_by_cook_time(self) -> List[Order]:
        return sorted(self.orders, key=lambda o: int(o.cook_time))

    def print_orders(self, orders: Iterator[Order] = None) -> None:
        """Выводит заказы. Если передан итератор/генератор, то печатает из него."""
        if orders is None:
            orders = self.iter_orders()
        count = 0
        for order in orders:
            print(order)
            count += 1
        if count == 0:
            print("Нет данных.")


class FileManager:
    """Класс для работы с файловой системой (пункт 1 из исходного задания)."""

    @staticmethod
    def list_files_generator(folder_path: str) -> Iterator[str]:
        """Генератор, возвращающий отсортированные имена файлов/папок в директории."""
        if not os.path.exists(folder_path):
            return
        for item in sorted(os.listdir(folder_path)):
            yield item

    @staticmethod
    def print_files(folder_path: str) -> None:
        """Выводит пронумерованный список файлов и их общее количество."""
        gen = FileManager.list_files_generator(folder_path)
        count = 0
        for i, name in enumerate(gen, start=1):
            print(i, name)
            count += 1
        print(f"Всего файлов в директории: {count}")


def get_files_menu():
    """Обработка пункта меню 1 (работа с директорией)."""
    while True:
        folder_path = input("Введите путь к директории: ")
        if os.path.exists(folder_path):
            print(f"Директория: {folder_path}")
            FileManager.print_files(folder_path)
            break
        else:
            print("Указанный путь не найден. Попробуйте снова.")


def main():
    manager = OrderManager()

    while True:
        print("\nВыберите пункт:")
        print("1. Количество файлов в директории")
        print("2. Информация о заказах")
        print("3. Информация о заказах, отсортированная по наименованию блюда")
        print("4. Информация о заказах, отсортированная по времени приготовления")
        print("5. Информация о заказах с отзывом, содержащим слово 'вкусно'")
        print("6. Добавить новый заказ")
        print("7. Выйти из программы")

        choice = input("Введите число от 1 до 7: ")
        if not choice.isdigit():
            print("Неверный ввод. Введите число.")
            continue
        choice = int(choice)

        if choice == 1:
            get_files_menu()
        elif choice in (2, 3, 4, 5, 6):
            manager.load_orders()  # Загружаем, если ещё не загружено, или заново
            if choice == 2:
                print("\nИнформация о заказах:")
                manager.print_orders()
            elif choice == 3:
                print("\nЗаказы, отсортированные по наименованию блюда:")
                sorted_orders = manager.sort_by_dish()
                manager.print_orders(iter(sorted_orders))  # передаём итератор
            elif choice == 4:
                print("\nЗаказы, отсортированные по времени приготовления:")
                sorted_orders = manager.sort_by_cook_time()
                manager.print_orders(iter(sorted_orders))
            elif choice == 5:
                print("\nЗаказы с отзывом, содержащим 'вкусно':")
                # Используем генератор прямо из класса
                filtered_gen = manager.filter_by_keyword_generator("вкусно")
                manager.print_orders(filtered_gen)
            elif choice == 6:
                manager.add_order()
        elif choice == 7:
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Введите число от 1 до 7.")


if __name__ == "__main__":
    main()