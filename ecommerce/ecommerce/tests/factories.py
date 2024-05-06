import factory
from ecommerce.product.models import Category, Brand, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # name = "test_category"     # test_category is here static data to be used for testing
    name = factory.sequence(lambda n: "test_category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.sequence(lambda n: "brand_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "product_name"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)          # since brand and category are relational field
    category = factory.SubFactory(CategoryFactory)