# Проект "Объектно-ориентированное программирование(ООП)"

---

## Оглавление
<a id="content"></a>
1. [Описание](#description)
2. [Установка и настройка проекта](#instruction)
3. [Структура проекта](#structure)
4. [Классы, примеры и тестирование](#class)
5. [Методы, декораторы, примеры и тестирование](#func)
6. [Модуль main для запуска и проверки проекта](#funcmain)
7. [Запуск и тестирование проекта](#launch)
8. [Лицензия](#license)

---

## Описание<a id="description"></a>
Проект представляет собой изучение ООП. В данном проекте реализовано два класса *Product* и *Category*. В классах
описаны атрибуты, реализованы инициализация экземпляров класса, методы, методы с декораторами. Для каждого класса
написаны тесты. Реализовано два подкласса класса *Product*. Это классы *Smartphone* и *LawnGrass*.
В проекте были реализованы абстрактный класс *BaseProduct* и класс миксин *PrintMixin*.
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
│ ├── base_product - в модуле находится абстрактный класс BaseProduct
│ ├── category.py - в модуле находится класс Category и инициализация экземпляра класса
│ ├── lawn_grass.py - в модуле находится подкласс LawnGrass класса Product
│ ├── print_mixin - в модуле находится класс миксин PrintMixin для вывода информации об экземпляре класса в консоль
│ ├── product - в модуле находится класс Product и инициализация экземпляра класса
│ ├── smartphone - в модуле находится подкласс Smartphone класса Product
├── tests - в папке находятся тесты для каждого модуля с классами
│ ├── __init__.py
│ ├── conftest.py
│ ├── test_category.py
│ ├── test_lawn_grass.py
│ ├── test_print_mixin.py
│ ├── test_product.py
│ ├── test_smartphone.py
├── .flake8
├── .gitignore
├── main.py - в модуле запускается проверка реализации классов
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## Классы, примеры их использования и тестирование<a id="class"></a>
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

3. Класс *LawnGrass* представляет категорию родительского класса Product. В классе реализованы атрибуты родительского
класса и доп. атрибуты данного класса: страна-производитель, срок прорастания, цвет.
Добавлен метод инициализации экземпляра класса с данными атрибутами.

```
Пример создания экземпляра класса:
grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

Пример проверки атрибутов экземпляра класса:
print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)
```
Класс протестирован в модуле *test_lawn_grass* в папке **tests**.

4. Класс *Smartphone* представляет категорию родительского класса Product. В классе реализованы атрибуты родительского
класса и доп. атрибуты данного класса: производительность, модель, объем встроенной памяти и цвет.
Добавлен метод инициализации экземпляра класса с данными атрибутами.

```
Пример создания экземпляра класса:
smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")

Пример проверки атрибутов экземпляра класса:
print(smartphone1.name)
print(smartphone1.description)
print(smartphone1.price)
print(smartphone1.quantity)
print(smartphone1.efficiency)
print(smartphone1.model)
print(smartphone1.memory)
print(smartphone1.color)
```
Класс протестирован в модуле *test_smartphone* в папке **tests**.

5. Класс миксин *PrintMixin* нужен для печати в консоль следующей информации об экземпляре класса
(класс, имя, описание, цена и количество). В классе реализован магический метод __repr__ и его вызов при
инициализации экземпляра класса.

```
Пример реализации метода:
def __init__(self):
    print(repr(self))

def __repr__(self):
    return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

Пример вывода информации:
Product(Iphone 15, 512GB, Gray space, 210000.0, 8)
```
Класс протестирован в модуле *test_print_mixin* в папке **tests**.

6. Абстрактный класс *BaseProduct*. В нем реализован абстрактный класс-метод для добавления нового продукта,
который используется во всех классах-наследниках.

---

## Методы, декораторы, примеры и тестирование<a id="func"></a>
### Методы, декораторы для класса Category
1. Метод *add_product* добавляет новый экземпляр класса Product в приватный список продуктов класса Category. Если
передается не экземпляр класса Product, то возбуждается ошибка TypeError.

```
Вызов метода: 
product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
category1.add_product(product4)

Пример проверки:
print(category1.name)
print(category1.price)
print(category1.product_count)
```
Метод протестирован в модуле *test_category* в папке **tests**.

2. Геттер *products* выводит список товаров в виде строк.

```
Вызов геттера: 
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)
print(category1.products)

Результат:
Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
```
Геттер протестирован в модуле *test_category* в папке **tests**.

3. Геттер *products_in_list* выводит список товаров. Используется для подсчета количества экземпляров класса в разных
категориях.

```
Вызов геттера: 
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)
print(len(category1.products_in_list))

Результат:
Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.

3
```
Геттер протестирован в модуле *test_category* в папке **tests**.

4. Метод *str* возвращает строку в формате "Название категории, количество продуктов: сумма шт."

```
Вызов геттера: 

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

print(str(product1))
print(str(product2))
print(str(product3))

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

print(str(category1))

Результат:

Смартфоны, количество продуктов: 27 шт.
```
Метод протестирован в модуле *test_category* в папке **tests**.

### Методы, декораторы для класса Product
1. Класс-метод *new_product* принимает на вход параметры товара в словаре и возвращает объект класса Product. Также
добавляет товар в список товаров, если товара с переданным именем не существует. Если имя существует, то суммирует
количество товара и устанавливает максимальную цену.

```
Вызов метода: 
new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
new_product_2 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 100000.0,
            "quantity": 3,
        }
    )

Пример проверки:
print(new_product.name)
print(new_product.description)
print(new_product.price)
print(new_product.quantity)
```
Метод протестирован в модуле *test_product* в папке **tests**.

2. Геттер *price* возвращает цену за выбранный товар.

```
Вызов геттера: 
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
print(product1.price)

Результат:
180000.0
```
Геттер протестирован в модуле *test_product* в папке **tests**.

3. Сеттер *price* обновляет цену товара, если переданная цена больше установленной. Если цена меньше установленной, то
уточняет у пользователя необходимость изменения цены в меньшую сторону. Если цена меньше 0 или равна 0, то выводит
сообщение "Цена не должна быть нулевая или отрицательная". 

```
Использование сеттера: 
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product1.price = 800
print(product1.price)

product1.price = 0
print(product1.price)

Результат:
Понизить цену товара? (y: yes / любой другой ответ: no): y
800
Цена не должна быть нулевая или отрицательная
```
Сеттер протестирован в модуле *test_product* в папке **tests**.

4. Статический метод *check_product_in_list* проверяет наличие товара по переданному имени. Если имя существует,
то суммирует кол-во и устанавливает максимальную цену. Если имя не найдено, то возвращает True-знак для добавления
товара в список.

```
Вызов метода: 
if check_product_in_list(name, price, quantity):
    ... - происходит добавление товара в список
    return cls(name, description, price, quantity)
else:
    return cls(name, description, price, quantity)
```
Метод протестирован в модуле *test_product* в папке **tests**.

5. Метод *str* выводит строку с продуктом в виде: Название продукта, сумма руб. Остаток: количество шт.

```
Использование метода: 
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
print(str(product1))


Результат:
Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
```
Метод протестирован в модуле *test_product* в папке **tests**.

6. Метод *add* возвращает полную стоимость всех товаров на складе выбранной категории товаров. Если выбраны товары
разной категории, то возбуждается ошибка TypeError.

```
Использование метода: 
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

print(product1 + product2)

Результат:
2580000.0
```
Метод протестирован в модуле *test_product* в папке **tests**.

---

## Модуль main для запуска и проверки проекта<a id="funcmain"></a>
1. Модуль *main* проверяет и возвращает созданные экземпляры классов Category и Product.
```
Вызов main:

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)

print(product2.name)
print(product2.description)
print(product2.price)
print(product2.quantity)

print(product3.name)
print(product3.description)
print(product3.price)
print(product3.quantity)

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

Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)
Product(Iphone 15, 512GB, Gray space, 210000.0, 8)
Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
Iphone 15
512GB, Gray space
210000.0
8
Xiaomi Redmi Note 11
1024GB, Синий
31000.0
14
True
Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
146
1
3
Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)
Телевизоры
Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником
42
55" QLED 4K, 123000.0 руб. Остаток: 7 шт.

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