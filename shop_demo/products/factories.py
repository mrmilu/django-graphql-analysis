# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports
import factory

# App imports
from shop_demo.products.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('product')
    description = factory.Faker('text')
