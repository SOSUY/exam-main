from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Product(AbstractProduct):
    def __init__(self, name: str, quantity: int, price: float):
        if price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self.name = name
        self.quantity = quantity
        self._price = price  # Приватное свойство

    def __add__(self, other):
        if isinstance(other, Product):
            total_quantity = self.quantity + other.quantity
            total_cost = self.quantity * self.get_price() + other.quantity * other.get_price()
            average_price = total_cost / total_quantity if total_quantity > 0 else 0
            return Product(f"{self.name} + {other.name}", total_quantity, average_price)
        else:
            raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.get_price() < other.get_price()
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.get_price() > other.get_price()
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.get_price()})"

    def get_description(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.get_price()})"

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self._price = new_price

class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        super().__init__(name, quantity, price)
        self.author = author

    def get_description(self):
        return f"Книга: {self.name}, Автор: {self.author}"

print("=== Тестирование Task 1 ===")
book1 = Book("Война и мир", 5, 500, "Лев Толстой")
book2 = Book("Преступление и наказание", 3, 450, "Фёдор Достоевский")

print(book1 + book2)
print(book1 > book2)  # True (500 > 450)
print(book1 < book2)  # False
try:
    invalid_book = Book("Ошибка", 1, -100, "Автор")
except ValueError as e:
    print(e)  # ValueError: Цена не может быть меньше нуля!

print("\n=== Тестирование Task 2 ===")
book = Book("Война и мир", 5, 500, "Лев Толстой")
print(book.get_description())  # "Книга: Война и мир, Автор: Лев Толстой"

print("\n=== Тестирование Task 3 ===")
print(f"Текущая цена: {book.get_price()}")
book.set_price(600)
print(f"Новая цена после set_price(600): {book.get_price()}")
try:
    book.set_price(-50)
except ValueError as e:
    print(e)  # ValueError: Цена не может быть меньше нуля!
print(f"Цена после попытки установить отрицательное значение: {book.get_price()}")

print("\n=== Дополнительное тестирование ===")
try:
    invalid_product = Product("Ошибка", 1, -200)
except ValueError as e:
    print(f"Создание продукта с отрицательной ценой: {e}")

product1 = Product("Товар 1", 2, 100)
product2 = Product("Товар 2", 1, 200)
print(f"product1 < product2: {product1 < product2}")
print(f"product1 > product2: {product1 > product2}")

result = product1 + product2
print(f"Сложение товаров: {result}")
