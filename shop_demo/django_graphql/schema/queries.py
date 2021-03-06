# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene

# App imports
from shop_demo.products.api.django_graphene.queries import ProductQuery


class Query(
    ProductQuery,
    graphene.ObjectType):
    pass
