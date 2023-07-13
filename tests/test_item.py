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
    """ Проверяем при скидке (0.8) конкретного товара"""
    items.apply_discount()
    Item.pay_rate = 0.8
    assert 10000 * Item.pay_rate == 8000.0
