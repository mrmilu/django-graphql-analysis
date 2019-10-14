# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
from ariadne import make_executable_schema, gql

# App imports
from shop_demo.products.api.ariadne.queries import query, query_defs
from shop_demo.products.api.ariadne.types import product, type_defs

ariadne_schema = make_executable_schema(gql(type_defs + query_defs), [query, product])