import csv
from src.instantiatecsverror import InstantiateCSVError




class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{str(self.__name)}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    # Геттер для name
    @property
    def name(self):
        """
        Выводим приватный атрибут name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Добавляем setter для name
        """
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        cls.all.clear()
        try:
            with open(filename, encoding='windows-1251', newline='', ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    if not name or not price or not quantity:   # Если файл `item.csv` поврежден (например, отсутствует одна из колонок данных) → выбрасывается исключение `InstantiateCSVError` с сообщением “_Файл item.csv поврежден_”.
                        raise InstantiateCSVError('Файл items.csv поврежден')
                    cls(name, price, quantity)
        except FileNotFoundError:       # Если файл `items.csv`, из которого по умолчанию считываются данные, не найден → выбрасывается исключение `FileNotFoundError` с сообщением “_Отсутствует файл item.csv_"
            print('Отсутствует файл items.csv')


    @staticmethod
    def string_to_number(str_all):
        """
        Возвращает число из числа-строки
        """

        return int(float(str_all))

    def __add__(self, other):
        """Сложение по количеству товара в магазине"""
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

