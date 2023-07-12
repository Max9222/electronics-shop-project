"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def items():
    return Item("Смартфон", 10000, 20)

def test_item_sum(items):
    """ Проверяем общую стоимотсть товара стоимость товара"""
    assert items.calculate_total_price() == 200000

def test_item_discount(items):
    """ Проверяем при скидке (скидки нет) конкретного товара"""
    assert items.apply_discount() == None