# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports
from django.test import testcases


class SchemaClientWithGQLContext(SchemaRequestFactory, Client):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self._schema = graphene_settings.SCHEMA

    def request(self, **request):
        request = WSGIRequest(self._base_environ(**request))

        if self.session:
            request.session = self.session
            request.user = get_user(request)
        return request

    def schema(self, **kwargs):
        self._schema = graphene.Schema(**kwargs)

    def execute(self, query, variables=None, **headers):
        request = self.post('/', **headers)
        context = GQLContext(request)
        request.META['HTTP_ACCEPT_LANGUAGE'] = request.META.get('Accept-Language', None)
        return super().execute(context, query, variables)


class SchemaTestCaseGQLContext(testcases.TestCase):
    client_class = SchemaClientWithGQLContext
