# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports
from ariadne import QueryType

from shop_demo.common.graphql import object_from_global_id
from shop_demo.products.models import Product

query = QueryType()

query_defs = """
    type Query {
        products: [Product!]!
        product(id: ID!): Product!
    }
"""


@query.field("products")
def resolve_products(*_):
    return Product.objects.all()


@query.field("product")
def resolve_products(*_, id=None):
    _type, _id = object_from_global_id(id)
    return Product.objects.get(id=_id)
