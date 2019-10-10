# -*- coding: utf-8 -*-
# Python imports

# Django imports
import quiz
from django.conf import settings

# 3rd Party imports
from rest_framework.test import APITestCase, RequestsClient

# App imports


class BaseTest(APITestCase):
    def execute(self, query):
        client = RequestsClient()
        endpoint = 'http://testserver/' + settings.GRAPHQL_ENDPOINT
        response = client.get(endpoint)
        if 'csrftoken' in response.cookies:
            client.headers.update({'X-CSRFToken': response.cookies['csrftoken']})

        result = quiz.execute(query, url=endpoint, client=client)
        return result
