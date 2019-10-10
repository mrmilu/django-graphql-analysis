# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports

# App imports
from ariadne import ObjectType

type_defs = """
    type Product {
        id: ID!
        name: String!
        description: String!
    }
"""

product = ObjectType("Product")
