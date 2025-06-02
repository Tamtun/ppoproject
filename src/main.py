from src.models import Product
from src.category import Category

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1 = Category(
        "Смартфоны", "Смартфоны для удобства жизни", [product1, product2, product3]
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))  # Теперь возвращает список, а не строку
    print(Category.total_categories)
    print(Category.total_products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры", "Современные телевизоры для комфорта", [product4]
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(
        "\n".join(str(product) for product in category2.products)
    )  # Теперь работает правильно

    print(Category.total_categories)
    print(Category.total_products)
