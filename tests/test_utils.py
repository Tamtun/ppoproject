import pytest
import json
from src.utils import load_categories_from_json, Category


@pytest.fixture
def sample_json(tmp_path):
    """Создает временный JSON-файл с тестовыми данными."""
    data = [
        {
            "name": "Категория1",
            "description": "Описание категории1",
            "products": [
                {
                    "name": "Товар1",
                    "description": "Описание1",
                    "price": 100.0,
                    "quantity": 5,
                },
                {
                    "name": "Товар2",
                    "description": "Описание2",
                    "price": 200.0,
                    "quantity": 3,
                },
            ],
        },
        {
            "name": "Категория2",
            "description": "Описание категории2",
            "products": [
                {
                    "name": "Товар3",
                    "description": "Описание3",
                    "price": 300.0,
                    "quantity": 2,
                }
            ],
        },
    ]

    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return file_path


def test_load_categories_from_json(sample_json):
    """Проверяет загрузку категорий из JSON-файла."""
    categories = load_categories_from_json(sample_json)

    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert isinstance(categories[1], Category)

    assert categories[0].name == "Категория1"
    assert categories[0].description == "Описание категории1"
    assert len(categories[0].products) == 2

    assert categories[1].name == "Категория2"
    assert categories[1].description == "Описание категории2"
    assert len(categories[1].products) == 1  # Убрали split("\n")


def test_product_attributes(sample_json):
    """Проверяет правильность данных товаров внутри категорий."""
    categories = load_categories_from_json(sample_json)

    product1 = categories[0].products[0]  # Теперь просто берем объект из списка
    product2 = categories[0].products[1]
    product3 = categories[1].products[0]

    assert product1.name == "Товар1"
    assert product2.name == "Товар2"
    assert product3.name == "Товар3"
