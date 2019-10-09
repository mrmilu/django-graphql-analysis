# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import pytest

# App imports
from shop_demo.django_graphql.schema import schema
from shop_demo.django_graphql.tests import object_global_id
from shop_demo.products.factories import ProductFactory
from shop_demo.products.tests.query_templates import QUERY_PRODUCT_LITE


@pytest.mark.django_db
def test_get_product():
    product = ProductFactory()
    query = QUERY_PRODUCT_LITE % object_global_id(product)
    expected = {
        "product": {
            "id": object_global_id(product),
            "name": product.name,
            "description": product.description
        }
    }
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected
