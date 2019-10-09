# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# App imports
from shop_demo.users.models import User

admin.site.register(User, UserAdmin)
