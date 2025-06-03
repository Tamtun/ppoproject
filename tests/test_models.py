import pytest
from src.models import Product, Smartphone, LawnGrass, BaseProduct


class TestBaseProduct:
    def test_base_product_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseProduct("Тестовый продукт", "Описание", 1000, 5)


class TestProduct:
    def test_product_creation(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert isinstance(product, BaseProduct)

    def test_product_zero_quantity(self):
        """Проверяет, выбрасывается ли ValueError при нулевом количестве товара."""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            Product("Бракованный товар", "Описание", 1000.0, 0)


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
