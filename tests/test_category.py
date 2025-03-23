from typing import Type

from src.category import Category


def test_category_init(smartphone_category: Type[Category], tv_category: Type[Category]) -> None:
    """Тест проверяет корректное создания экземпляра класса Category с атрибутами name, description, products. Также
    тест проверяет корректный подсчет количества категорий и количества продуктов в этой категории"""
    assert smartphone_category.name == "Смартфоны"
    assert (
        smartphone_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
    )
    assert len(smartphone_category.products_in_list) == 3

    assert tv_category.name == "Телевизоры"
    assert tv_category.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert len(tv_category.products_in_list) == 1

    assert smartphone_category.category_count == 2
    assert tv_category.category_count == 2

    assert smartphone_category.product_count == 4
    assert tv_category.product_count == 4
