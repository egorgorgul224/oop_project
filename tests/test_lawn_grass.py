import pytest

from src.lawn_grass import LawnGrass


def test_lawn_grass_init(lawn_grass: LawnGrass) -> None:
    """Тест проверяет корректное создания экземпляра класса-наследника Smartphone."""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_lawn_grass_add(lawn_grass: LawnGrass, lawn_grass_another: LawnGrass) -> None:
    """Тест проверяет корректное сложение и вывод общей суммы всего товара категории LawnGrass."""
    assert lawn_grass + lawn_grass_another == 16750


def test_lawn_grass_add_error(lawn_grass: LawnGrass, lawn_grass_another: LawnGrass) -> None:
    """Тест проверяет корректный вывод ошибки TypeError, если пытаются сложить данные не подкласса LawnGrass."""
    with pytest.raises(TypeError):
        assert lawn_grass + 1
