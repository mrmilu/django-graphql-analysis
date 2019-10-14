# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import strawberry

# App imports
from shop_demo.products.api.strawberry.queries import Query

strawberry_schema = strawberry.Schema(query=Query)
