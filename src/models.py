class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products_list=None):
        """Создаёт новый товар с проверкой дубликатов"""
        if products_list:
            for prod in products_list:
                if prod.name.lower() == product_data["name"].lower():
                    prod.quantity += product_data["quantity"]
                    prod.price = max(prod.price, product_data["price"])
                    return prod
        return cls(**product_data)

    @property
    def price(self):
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if hasattr(self, "_Product__price") and new_price < self.__price:
            confirm = input(
                f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product):
        """Добавляет товар в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        """Геттер для форматированного вывода товаров"""
        return "\n".join(
            [
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
                for p in self.__products
            ]
        )

    @property
    def product_count(self):
        """Количество товаров в категории (для совместимости)"""
        return len(self.__products)
