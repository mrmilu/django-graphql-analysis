# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports
from ariadne import QueryType

from shop_demo.products.models import Product

query = QueryType()

query_defs = """
    type Query {
        products: [Product!]!
    }
"""


# Resolvers are simple python functions
@query.field("products")
def resolve_products(*_):
    return Product.objects.all()
