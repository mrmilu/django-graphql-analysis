# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
from ariadne import ObjectType

# App imports
from shop_demo.common.graphql import object_global_id

type_defs = """
    type Product {
        id: ID!
        name: String!
        description: String!
    }
"""

product = ObjectType("Product")


@product.field("id")
def resolve_id(obj, info):
    return object_global_id(obj)


@product.field("name")
def resolve_id(obj, info):
    return obj.name


@product.field("description")
def resolve_id(obj, info):
    return obj.description
