"""graphql_demos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DJANGO_GRAPHQL:
    from graphene_django.views import GraphQLView as DjangoGraphQLView

    urlpatterns += [path(settings.GRAPHQL_ENDPOINT, DjangoGraphQLView.as_view(graphiql=True), name='django-graphql')]

if settings.ARIADNE:
    from ariadne.contrib.django.views import GraphQLView as AriadneGraphQLView
    from shop_demo.ariadne.schema import ariadne_schema

    urlpatterns += [path(settings.GRAPHQL_ENDPOINT, AriadneGraphQLView.as_view(schema=ariadne_schema), name='ariadne'), ]

if settings.STRAWBERRY:
    from strawberry.contrib.django.views import GraphQLView as StrawberryGraphQLView
    from shop_demo.strawberry.schema import strawberry_schema

    urlpatterns += [path(settings.GRAPHQL_ENDPOINT, StrawberryGraphQLView.as_view(schema=strawberry_schema), name='strawberry'), ]
