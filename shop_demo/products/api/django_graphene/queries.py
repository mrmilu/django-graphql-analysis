# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene
from graphene_django.filter import DjangoFilterConnectionField

# App imports
from shop_demo.products.api.django_graphene.types import ProductType


class ProductQuery(graphene.ObjectType):
    products = DjangoFilterConnectionField(ProductType)
    product = graphene.relay.Node.Field(ProductType)
