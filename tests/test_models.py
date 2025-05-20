import pytest
from unittest.mock import patch
from src.models import Product, Category


@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Гаджеты", [sample_product])


class TestProduct:
    """Тесты для класса Product."""

    def test_product_init(self, sample_product):
        """Проверка корректности инициализации Product."""
        assert sample_product.name == "Телефон"
        assert sample_product.description == "Смартфон"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10

    def test_private_price_access(self, sample_product):
        """Проверка приватности атрибута цены."""
        with pytest.raises(AttributeError):
            print(sample_product.__price)

    def test_price_property(self, sample_product):
        """Проверка работы геттера цены."""
        assert sample_product.price == 50000.0

    def test_price_setter_validation(self, sample_product, capsys):
        """Проверка валидации цены в сеттере."""
        sample_product.price = -100
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert sample_product.price == 50000.0

    def test_price_decrease_confirmation(self, sample_product):
        """Проверка подтверждения снижения цены через input."""
        with patch("builtins.input", return_value="y"):
            sample_product.price = 40000.0
            assert sample_product.price == 40000.0

    def test_price_decrease_cancellation(self, sample_product, capsys):
        """Проверка отмены снижения цены через input."""
        original_price = sample_product.price
        with patch("builtins.input", return_value="n"):
            sample_product.price = 40000.0
            captured = capsys.readouterr()
            assert "Изменение цены отменено" in captured.out
            assert sample_product.price == original_price

    def test_new_product_classmethod(self):
        """Проверка создания товара через класс-метод."""
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой",
            "price": 100000.0,
            "quantity": 5,
        }
        product = Product.new_product(product_data)
        assert isinstance(product, Product)
        assert product.name == "Ноутбук"

    def test_new_product_with_duplicate(self):
        """Проверка обработки дубликатов в new_product."""
        existing_product = Product("Мышь", "Беспроводная", 2500.0, 10)
        product_data = {
            "name": "Мышь",
            "description": "Новая модель",
            "price": 3000.0,
            "quantity": 5,
        }
        product = Product.new_product(product_data, [existing_product])
        assert product.quantity == 15
        assert product.price == 3000.0

    def test_new_product_with_empty_list(self):
        """Проверка new_product с пустым списком товаров."""
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой",
            "price": 100000.0,
            "quantity": 5,
        }
        product = Product.new_product(product_data, [])
        assert product.name == "Ноутбук"


class TestCategory:
    """Тесты для класса Category."""

    def test_category_init(self, sample_category, sample_product):
        """Проверка корректности инициализации Category."""
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Гаджеты"
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in sample_category.products

    def test_private_products_access(self, sample_category):
        """Проверка приватности атрибута products."""
        with pytest.raises(AttributeError):
            print(sample_category.__products)

    def test_add_product_method(self, sample_category):
        """Проверка метода add_product."""
        initial_count = Category.total_products
        new_product = Product("Планшет", "10 дюймов", 30000.0, 8)
        sample_category.add_product(new_product)
        assert Category.total_products == initial_count + 1
        assert "Планшет, 30000.0 руб. Остаток: 8 шт." in sample_category.products

    def test_add_product_type_check(self, sample_category):
        """Проверка обработки неверного типа в add_product."""
        with pytest.raises(TypeError) as excinfo:
            sample_category.add_product("not a product")
        assert "Можно добавлять только объекты класса Product" in str(excinfo.value)

    def test_products_property_format(self, sample_category):
        """Проверка формата вывода products property."""
        output = sample_category.products
        assert output == "Телефон, 50000.0 руб. Остаток: 10 шт."

    def test_products_property_with_multiple(self):
        """Проверка products property с несколькими товарами."""
        p1 = Product("Товар 1", "Описание", 100.0, 5)
        p2 = Product("Товар 2", "Описание", 200.0, 3)
        category = Category("Категория", "Описание", [p1, p2])

        output = category.products
        assert "Товар 1, 100.0 руб. Остаток: 5 шт." in output
        assert "Товар 2, 200.0 руб. Остаток: 3 шт." in output
        assert len(output.split("\n")) == 2

    def test_counters(self):
        """Проверка подсчёта количества категорий и товаров."""
        Category.total_categories = 0
        Category.total_products = 0

        product1 = Product("Товар 1", "Описание", 100.0, 5)
        product2 = Product("Товар 2", "Описание", 200.0, 3)

        category = Category("Категория", "Описание", [product1, product2])

        assert Category.total_categories == 1
        assert Category.total_products == 2

    def test_product_count_property(self):
        """Проверка свойства product_count в Category."""
        product1 = Product("Товар 1", "Описание 1", 100.0, 5)
        product2 = Product("Товар 2", "Описание 2", 200.0, 3)

        # Создаем категорию с 2 товарами
        category = Category("Тестовая категория", "Описание", [product1, product2])

        assert category.product_count == 2

        product3 = Product("Товар 3", "Описание 3", 300.0, 1)
        category.add_product(product3)
        assert category.product_count == 3


def test_json_loading():
    """Проверка загрузки данных из JSON (доп. задание)."""
    from src.utils import load_categories_from_json
    import os

    if os.path.exists("data/products.json"):
        categories = load_categories_from_json("data/products.json")
        assert isinstance(categories, list)
        if categories:
            assert isinstance(categories[0], Category)
