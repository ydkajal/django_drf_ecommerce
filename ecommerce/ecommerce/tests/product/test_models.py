import pytest

pytestmark = pytest.mark.django_db           # globally defining for all test cases to allow access to db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange---arrange all data that is required to test. Get data from
        # testing database
        # Act--act on the data arranged
        x = category_factory(name="test_cat")   # overriding name
        # Aseert --check data with the expected result
        assert x.__str__() == 'test_cat'  


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange---arrange all data that is required to test. Get data from
        # testing database
        # Act--act on the data arranged
        x = brand_factory(name="brand_name")   # overriding name
        # Aseert --check data with the expected result
        assert x.__str__() == 'brand_name'


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange---arrange all data that is required to test. Get data from
        # testing database
        # Act--act on the data arranged
        x = product_factory(name="product_name")   # overriding name
        # Aseert --check data with the expected result
        assert x.__str__() == 'product_name'