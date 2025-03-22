# Проект "Объектно-ориентированное программирование(ООП)"

---

## Оглавление
<a id="content"></a>
1. [Описание](#description)
2. [Установка и настройка проекта](#instruction)
3. [Структура проекта](#structure)
4. [Классы, примеры и тестирование](#func)
5. [Модуль main для запуска и проверки проекта](#funcmain)
6. [Запуск и тестирование проекта](#launch)
7. [Лицензия](#license)

---

## Описание<a id="description"></a>
Проект представляет собой изучение ООП. В данном проекте реализовано два класса *Product* и *Category*. В классах
описаны атрибуты, реализована инициализация экземпляров класса. Для каждого класса написаны тесты.

---

## Установка и настройка проекта<a id="instruction"></a>

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Перейдите в директорию проекта:
```
cd ваш_проект
```
3. Установите зависимости проекта:
```
poetry install
```

---

## Структура проекта<a id="structure"></a>
```
.
├── src
│ ├── __init__.py
│ ├── category.py - в модуле находится класс Category и инициализация экземпляра класса
│ ├── product - в модуле находится класс Product и инициализация экземпляра класса
├── tests - в папке находятся тесты для каждого модуля с классами
│ ├── __init__.py
│ ├── conftest.py
│ ├── test_category.py
│ ├── test_product.py
├── .flake8
├── .gitignore
├── main.py - в модуле запускается проверка реализации классов
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## Классы, примеры их использования и тестирование<a id="func"></a>
1. Класс *Category* представляет категорию продукта. В классе реализованы атрибуты: имя, описание, список продуктов в
каждой категории, количество категорий в классе, количество продуктов в классе. Добавлен метод инициализации экземпляра
класса с данными атрибутами.

```
Пример создания экземпляра класса:
category2 = Category("Имя_категории", "Описание_категории", [продукт_1, продукт_2,...])

Пример проверки атрибутов экземпляра класса:
print(category2.name)
print(category2.description)
print(len(category2.products))
print(category2.products)

Пример проверки атрибутов класса:
print(Category.category_count)
print(Category.product_count)
```
Класс протестирован в модуле *test_category* в папке **tests**.

2. Класс *Product* представляет продукт. В классе реализованы атрибуты: имя, описание, цена, количество.
Добавлен метод инициализации экземпляра класса с данными атрибутами.

```
Пример создания экземпляра класса:
product1 = Product("Имя_продукта", "Описание_продукта", цена_продукта, количество)

Пример проверки атрибутов экземпляра класса:
print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)
```
Класс протестирован в модуле *test_product* в папке **tests**.

---

### Модуль main для запуска и проверки проекта<a id="funcmain"></a>
1. Модуль *main* проверяет и возвращает созданные экземпляры классов Category и Product.
```
Вызов main:
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)

print(product2.name)
print(product2.description)
print(product2.price)
print(product2.quantity)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

print(category1.name == "Смартфоны")
print(category1.description)
print(len(category1.products))
print(category1.category_count)
print(category1.product_count)

product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product4],
)

print(category2.name)
print(category2.description)
print(len(category2.products))
print(category2.products)

print(Category.category_count)
print(Category.product_count)
```
```
Результат:
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
Iphone 15
512GB, Gray space
210000.0
8
True
Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
3
1
3
Телевизоры
Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником
1
[<src.product.Product object at 0x0000021ACDCE9E00>]
2
4
```

---

## Запуск и тестирование проекта<a id="launch"></a>
1. После установки и настройки проекта перейти в модуль main в корне проекта.
2. Запустить его с помощью кнопки *run* или консоли *python/python3 main.py*.

---

## Лицензия<a id="license"></a>

Этот проект лицензирован по [лицензии MIT](LICENSE).

##### [Оглавление](#content)