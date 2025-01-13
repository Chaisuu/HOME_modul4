def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получения дополнительных функций для удобства жизни")
    assert category.products == ["product1", "product2", "product3"]
    assert category.count_of_categories == 1
    assert category.count_of_products == 3


def test_category_empty_products(empty_product_in_categoty):
    assert empty_product_in_categoty.count_of_products == 3
    assert empty_product_in_categoty.count_of_categories == 2
