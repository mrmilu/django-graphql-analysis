# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.conf import settings

# 3rd Party imports
import pytest

# App
from shop_demo.common.graphql import object_global_id
from shop_demo.products.tests.base import BaseTest

if settings.DJANGO_GRAPHQL:
    from shop_demo.django_graphql.schema import schema
if settings.ARIADNE:
    from shop_demo.ariadne.schema import ariadne_schema as schema

from shop_demo.products.factories import ProductFactory
from shop_demo.products.tests.query_templates import QUERY_PRODUCT_LITE


class GetProductsTest(BaseTest):

    def setUp(self):
        product = ProductFactory()

        self.expected = {
            "product": {
                "id": object_global_id(product),
                "name": product.name,
                "description": product.description
            }
        }
        self.query = QUERY_PRODUCT_LITE % object_global_id(product)

    @pytest.mark.django_db
    def test_query(self):
        result = self.execute(self.query)
        assert result == self.expected
