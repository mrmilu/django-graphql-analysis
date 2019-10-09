# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.utils.decorators import classonlymethod
from django.views.decorators.csrf import csrf_exempt

# 3rd Party imports
from graphene_django.views import GraphQLView as BaseGraphQLView

# App imports
from shop_demo.django_graphql.context import GQLContext


# class GraphQLView(LoginRequiredMixin, BaseGraphQLView):
class GraphQLView(BaseGraphQLView):

    @classonlymethod
    def as_view(cls, **initkwargs):
        fn = super(GraphQLView, cls).as_view(**initkwargs)
        return csrf_exempt(fn)

    def get_context(self, request):
        return GQLContext(request)
