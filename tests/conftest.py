import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products=["product1", "product2", "product3"])


@pytest.fixture
def empty_product_in_categoty():
    return Category(name="Телевизоры",
                    description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
