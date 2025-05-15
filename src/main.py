from src.models import Product, Category
from src.utils import load_categories_from_json
# Добавлен комментарий для pull request
if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("=== Созданные вручную товары ===")
    for product in [product1, product2, product3]:
        print(f"{product.name}, Цена: {product.price} руб.")

    category1 = Category(
        "Смартфоны", "Средство коммуникации и не только", [product1, product2, product3]
    )

    print("\n=== Категория 1 (Смартфоны) ===")
    print(f"Товаров в категории: {len(category1.products)}")

    """ Загрузка данных из JSON """
    print("\n=== Загрузка данных из JSON ===")
    try:
        # Загружаем категории из файла
        json_categories = load_categories_from_json("../data/products.json")

        # Выводим информацию о загруженных категориях
        for category in json_categories:
            print(f"\nКатегория: {category.name}")
            print(f"Товаров: {len(category.products)}")
            for product in category.products:
                print(f"  - {product.name}, Цена: {product.price}")

        print(f"\nИтого загружено категорий: {len(json_categories)}")
    except FileNotFoundError:
        print("Ошибка: файл 'data/products.json' не найден!")

    """ Итоговая статистика """
    print("\n=== Общая статистика ===")
    print(f"Всего категорий в программе: {Category.total_categories}")
    print(f"Всего товаров в программе: {Category.total_products}")
