# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
# import snug
from graphql_extensions.testcases import SchemaTestCase
from graphql_relay import to_global_id


# App imports


class BaseTest(SchemaTestCase):
    pass


def object_global_id(obj):
    return to_global_id(obj._meta.model_name, obj.id)
