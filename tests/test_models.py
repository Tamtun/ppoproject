import pytest
from src.models import Product, Category

@pytest.fixture(autouse=True)
def reset_category_products():
    """Сбрасывает счетчик total_products перед каждым тестом."""
    Category.total_products = 0

@pytest.fixture
def sample_product():
    return Product("Товар1", "Описание товара", 100.0, 5)

@pytest.fixture
def another_product():
    return Product("Товар2", "Описание другого товара", 200.0, 3)

@pytest.fixture
def sample_category(sample_product, another_product):
    return Category("Категория1", "Описание категории", [sample_product, another_product])

def test_category_add_invalid_product(sample_category):
    """Проверяем, что передача некорректного объекта вызывает TypeError."""
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        sample_category.add_product("не продукт")  # Передаем строку вместо объекта Product


def test_category_iteration(sample_category):
    """Проверяем, что объект Category можно итерировать."""
    iterator = iter(sample_category)
    assert hasattr(iterator, "__next__")  # Проверяем, что у объекта есть метод __next__

    product_names = [product.name for product in iterator]
    assert product_names == ["Товар1", "Товар2"]

def test_product_initialization(sample_product):
    assert sample_product.name == "Товар1"
    assert sample_product.description == "Описание товара"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 5

def test_product_str(sample_product):
    assert str(sample_product) == "Товар1, 100.0 руб. Остаток: 5 шт."

def test_product_addition(sample_product, another_product):
    assert sample_product + another_product == (100.0 * 5) + (200.0 * 3)

    with pytest.raises(TypeError):
        sample_product + "не продукт"

def test_product_price_setter(sample_product):
    sample_product.price = 150.0
    assert sample_product.price == 150.0

    sample_product.price = -50.0
    assert sample_product.price != -50.0  # Проверяем, что цена не изменилась на отрицательную

def test_category_initialization(sample_category):
    assert sample_category.name == "Категория1"
    assert sample_category.description == "Описание категории"
    assert len(sample_category.products.split("\n")) == 2

def test_category_str(sample_category):
    assert str(sample_category) == "Категория1, количество продуктов: 8 шт."

def test_category_add_product(sample_category):
    new_product = Product("Товар3", "Еще один товар", 300.0, 2)
    initial_count = Category.total_products  # Запоминаем количество продуктов до добавления
    sample_category.add_product(new_product)

    assert "Товар3" in sample_category.products
    assert Category.total_products == initial_count + 1  # Проверяем, что счетчик увеличился корректно

def test_category_iterator(sample_category):
    product_names = [product.name for product in sample_category]
    assert product_names == ["Товар1", "Товар2"]

