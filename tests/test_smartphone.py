import pytest

from src.smartphone import Smartphone


def test_smartphone_init(smartphone_product: Smartphone) -> None:
    """Тест проверяет корректное создания экземпляра класса-наследника Smartphone."""
    assert smartphone_product.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product.price == 180000.0
    assert smartphone_product.quantity == 5
    assert smartphone_product.efficiency == 95.5
    assert smartphone_product.model == "S23 Ultra"
    assert smartphone_product.memory == 256
    assert smartphone_product.color == "Серый"


def test_smartphone_add(smartphone_product: Smartphone, smartphone_product_another: Smartphone) -> None:
    """Тест проверяет корректное сложение и вывод общей суммы всего товара категории Smartphone."""
    assert smartphone_product + smartphone_product_another == 2580000


def test_smartphone_add_error(smartphone_product: Smartphone, smartphone_product_another: Smartphone) -> None:
    """Тест проверяет корректный вывод ошибки TypeError, если пытаются сложить данные не подкласса Smartphone."""
    with pytest.raises(TypeError):
        assert smartphone_product + 1
