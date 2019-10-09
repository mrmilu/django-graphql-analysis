# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.contrib import admin

# App imports
from shop_demo.products.models import Product


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
