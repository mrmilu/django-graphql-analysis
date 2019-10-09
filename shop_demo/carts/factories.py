# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports
import factory

# App imports
from shop_demo.carts.models import Cart


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart

    name = factory.Faker('cart')
    description = factory.Faker('text')
