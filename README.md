# Каталог товаров (Python OOP)

Проект реализует систему управления товарами и категориями с:
- Классами `Product` и `Category`
- Автоматическим подсчётом товаров/категорий
- Загрузкой данных из JSON
- Тестами с покрытием > 75%

## Структура проекта
```
.
├── src/
│   ├── __init__.py
│   ├── models.py       # Классы Product и Category
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
poetry run python src/main.py
```

## Тесты:

```bash
poetry run pytest --cov=src
```