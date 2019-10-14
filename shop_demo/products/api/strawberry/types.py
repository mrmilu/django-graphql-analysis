# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports
import strawberry


# App imports


@strawberry.type
class Product:
    id: str
    name: str
    description: str
