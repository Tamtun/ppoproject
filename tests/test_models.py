import pytest
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


class TestCategory:
    """Тесты для класса Category."""

    def test_category_init(self, sample_category, sample_product):
        """Проверка корректности инициализации Category."""
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Гаджеты"
        assert sample_category.products == [sample_product]

    def test_counters(self):
        """Проверка подсчёта количества категорий и товаров."""
        # Сброс счётчиков на случай предыдущих тестов
        Category.total_categories = 0
        Category.total_products = 0

        product1 = Product("Товар 1", "Описание", 100.0, 5)
        product2 = Product("Товар 2", "Описание", 200.0, 3)

        category = Category("Категория", "Описание", [product1, product2])

        assert Category.total_categories == 1
        assert Category.total_products == 2


def test_json_loading():
    """Проверка загрузки данных из JSON (доп. задание)."""
    from src.utils import load_categories_from_json
    import os

    if os.path.exists("data/products.json"):
        categories = load_categories_from_json("data/products.json")
        assert isinstance(categories, list)
        if categories:
            assert isinstance(categories[0], Category)