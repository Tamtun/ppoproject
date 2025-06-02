# Каталог товаров (Python OOP)

Проект реализует систему управления товарами и категориями с:
- Классами `Product`, `Smartphone`, `LawnGrass`, `Order` и `Category`
- Миксином `ProductMixin`, который выводит информацию о созданном объекте в консоль
- Автоматическим подсчётом товаров/категорий
- Загрузкой данных из JSON (`utils.py`)
- Ограничением сложения товаров разных типов (`TypeError`)
- Тестами с покрытием **91%**, включая проверки `__str__` и `__iter__` 

## Структура проекта
```
.
├── src/
│   ├── __init__.py
│   ├── models.py       # Класс Product
│   ├── category.py     # Класс Category
│   ├── utils.py        # Загрузка из JSON
│   └── main.py         # Точка входа (запуск программы)
├── tests/
│   ├── __init__.py
│   └── test_models.py  # Тесты
├── data/
│   └── products.json   # Пример данных
├── README.md           # Документация
└── pyproject.toml      # Зависимости Poetry
```

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/tamtun/python-product-catalog.git
   
2. Установите зависимости:
   ```bash
   poetry install

## Запуск
Основной скрипт:

```bash
poetry run python -m src.main
```

## Тесты:

```bash
poetry run pytest --cov=src
```

## Покрытие тестами:

```bash
poetry run coverage run -m pytest
poetry run coverage report
```
Если нужен HTML-отчет::

```bash
poetry run coverage html
```