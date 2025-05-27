import pytest
from src.models import Product, Smartphone, LawnGrass, Category


class TestProduct:
    def test_product_init(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_price_setter(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = 60000.0
        assert product.price == 60000.0
        product.price = -100
        assert product.price == 60000.0

    def test_str_representation(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


class TestSmartphone:
    def test_smartphone_creation(self):
        phone = Smartphone("iPhone", "Флагман", 100000, 5, 95.5, "15 Pro", 256, "Black")
        assert phone.name == "iPhone"
        assert phone.model == "15 Pro"
        assert phone.memory == 256
        assert isinstance(phone, Product)


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        grass = LawnGrass("Трава", "Газонная", 500, 20, "Россия", "14 дней", "Зелёная")
        assert grass.country == "Россия"
        assert grass.germination_period == "14 дней"
        assert isinstance(grass, Product)


class TestCategory:
    def setup_class(self):
        Category.total_categories = 0
        Category.total_products = 0

    def test_category_creation(self):
        p = Product("Товар", "Описание", 100, 5)
        category = Category("Категория", "Описание", [p])
        assert category.name == "Категория"
        assert category.product_count == 1

    def test_add_product(self):
        category = Category("Категория", "Описание", [])
        p = Product("Товар", "Описание", 100, 5)
        category.add_product(p)
        assert category.product_count == 1

    def test_add_invalid_product(self):
        category = Category("Категория", "Описание", [])
        with pytest.raises(TypeError):
            category.add_product("Не продукт")

    def test_str_representation(self):
        p1 = Product("Товар 1", "Описание", 100, 5)
        p2 = Product("Товар 2", "Описание", 200, 3)
        category = Category("Категория", "Описание", [p1, p2])
        assert str(category) == "Категория, количество продуктов: 8 шт."

    def test_category_iteration(self):
        p1 = Product("Товар 1", "Описание", 100, 5)
        p2 = Product("Товар 2", "Описание", 200, 3)
        category = Category("Категория", "Описание", [p1, p2])
        assert list(category) == [p1, p2]


class TestAddition:
    def test_valid_addition(self):
        p1 = Smartphone("Phone1", "", 1000, 2, 90.0, "X", 128, "Black")
        p2 = Smartphone("Phone2", "", 2000, 3, 95.0, "Y", 256, "White")
        assert p1 + p2 == 1000 * 2 + 2000 * 3

    def test_invalid_addition(self):
        phone = Smartphone("Phone", "", 1000, 2, 90.0, "X", 128, "Black")
        grass = LawnGrass("Grass", "", 500, 3, "Россия", "14 дней", "Зелёная")
        with pytest.raises(TypeError):
            phone + grass
