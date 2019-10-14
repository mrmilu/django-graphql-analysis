from shop_demo.config.settings.base import *

INSTALLED_APPS += ['strawberry.contrib.django']

STRAWBERRY = True
GRAPHQL_ENDPOINT = 'strawberry'
