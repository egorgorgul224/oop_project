from src.product import Product


class LawnGrass(Product):
    """Класс-наследник для представления продукта категории трава газонная.
    Класс содержит следующие свойства: название (name: str), описание (description: str), цена (__price: float),
    количество в наличии (quantity: int), страна-производитель (country: str),
    срок прорастания (germination_period: str), цвет (color: str).
    """

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод для инициализации экземпляра класса LawnGrass. Задает значения атрибутам экземпляра. Добавляет
        экземпляр класса в список продуктов."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
