# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.contrib import admin

# App imports
from shop_demo.carts.models import Cart


class CartAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)
