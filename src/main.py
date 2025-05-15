from models import Product, Category

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны как средство коммуникации",
        [product1, product2, product3],
    )

    print("=== Все товары в категории ===")
    print(category1.products)

    print("\n=== Добавляем новый товар ===")
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)

    print("\n=== Количество товаров ===")
    print(f"В категории: {category1.product_count}")
    print(f"Всего товаров: {Category.total_products}")

    print("\n=== Тест класс-метода ===")
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет",
            "price": 185000.0,
            "quantity": 3,
        }
    )
    print(f"Новый товар: {new_product.name}, {new_product.price} руб.")

    print("\n=== Тест изменения цены ===")
    new_product.price = -100
    print(f"Текущая цена: {new_product.price}")
    new_product.price = 170000
    print(f"Новая цена: {new_product.price}")
