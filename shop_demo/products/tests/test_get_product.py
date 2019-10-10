# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import json
import quiz
import pytest
from rest_framework.test import RequestsClient

# App imports
from shop_demo.django_graphql.schema import schema
from shop_demo.django_graphql.tests import object_global_id, BaseTest
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
    def test_schema(self):
        result = schema.execute(self.query)
        assert not result.errors
        assert result.data == self.expected

    @pytest.mark.django_db
    def test_quiz(self):
        client = RequestsClient()
        response = client.get('http://testserver/django-graphql')
        client.headers.update({'X-CSRFToken': response.cookies['csrftoken']})

        result = quiz.execute(self.query, url='http://testserver/django-graphql', client=client)
        assert result == self.expected

    @pytest.mark.django_db
    def test_requests(self):
        client = RequestsClient()
        response = client.get('http://testserver/django-graphql')
        csrftoken = response.cookies['csrftoken']

        response = client.post('http://testserver/django-graphql', data={"query": self.query},
                               headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 200
        assert json.loads(response.content)['data'] == self.expected

    @pytest.mark.django_db
    def test_schema_client(self):
        response = self.client.execute(self.query)
        assert response.errors is None
        assert response.data == self.expected
