from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Инициализируем атрибут number_of_sim = количество поддерживаемых сим-карт
        self.number_of_sim = number_of_sim

    def __repr__(self):
        # Переопределил метод (добавил - number_of_sim)
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"





