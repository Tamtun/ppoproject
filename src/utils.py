import json
from pathlib import Path
from typing import List
from .models import Product

# from src.category import Category
from src.category import Category  # Вместо ".category"


def load_categories_from_json(file_path: str | Path) -> List[Category]:
    """
    Загружает категории и товары из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Список объектов Category.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            for product_data in category_data["products"]
        ]
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
