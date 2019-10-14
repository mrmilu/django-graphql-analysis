# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports
import strawberry

# App imports
from shop_demo.common.graphql import object_from_global_id, object_global_id
from shop_demo.products.api.strawberry.types import Product as ProductType
from shop_demo.products.models import Product


@strawberry.type
class Query:
    @strawberry.field
    def product(self, info, id: str) -> ProductType:
        _type, _id = object_from_global_id(id)
        product = Product.objects.get(id=_id)
        return ProductType(id=object_global_id(product), name=product.name, description=product.description)
