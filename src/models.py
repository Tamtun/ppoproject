class Product:
    """Класс для представления товара."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация товара.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    """Класс для представления категории товаров."""

    total_categories = 0  # Атрибут класса: общее количество категорий
    total_products = 0  # Атрибут класса: общее количество товаров

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Инициализация категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров (объектов Product).
        """
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1
        Category.total_products += len(products)
