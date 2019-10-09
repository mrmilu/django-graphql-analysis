# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene
from graphene_django import DjangoObjectType

# App imports
from shop_demo.products.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        # name = 'product'
        model = Product
        interfaces = (graphene.relay.Node,)
        # # connection_class = CountableConnectionBase
        # only_fields = [
        #     'id',
        #     'created',
        #     'modified',
        #     'name',
        #     'description',
        # ]
        filter_fields = [
            'id',
            'name'
        ]
