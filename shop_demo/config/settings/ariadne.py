from shop_demo.config.settings.base import *

INSTALLED_APPS += ["ariadne.contrib.django"]

ARIADNE = True
GRAPHQL_ENDPOINT = 'ariadne'
