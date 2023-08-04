"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.instantiatecsverror import InstantiateCSVError

from src.item import Item


@pytest.mark.parametrize(
    ('discount', 'price_with_discount'), [
        (0, 10_000),
        (0.15, 8_500),
        (0.27, 7_300),
    ]
)
def test_apply_discount(discount, price_with_discount):
    item = Item('test_item', 10_000, 20)
    Item.pay_rate = 1 - discount

    # Тест полная цена товара

    assert item.calculate_total_price() == 20_0000

    item.apply_discount()
    # Тест Цена со скидкой
    assert item.price == price_with_discount

    # Тест c именем "test_item"
    assert item.name == "test_item"

    # Тест c именем "maxoog"
    item.name = "maxoog"
    assert item.name == "maxoog"

    # Тест name.setter
    item.name = "Электро-самокат"
    assert item.name == "Электро-са"

    # Тест для instantiate_from_csv()
    item1 = Item.instantiate_from_csv()
    assert isinstance(item, Item)


    # Тест для string_to_number
    item2 = Item.string_to_number("as sdf sdf 60")
    assert item2 == 60

    # Тест для repr и str
    item1 = Item("Кулек", 50000, 70)
    assert repr(item1) == "Item('Кулек', 50000, 70)"
    assert str(item1) == 'Кулек'

    # Тест для метода __add__
    item3 = Item("Смартфон", 10000, 20)
    assert item3 + item1 == 90


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError) as file:
        Item.instantiate_from_csv('itemss.csv')
    assert str(file.value) == 'Отсутствует файл item.csv'
