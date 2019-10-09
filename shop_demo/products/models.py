# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Third party imports
from djmoney.models.fields import MoneyField

# App imports
from shop_demo.products.mixins import VariantMixin


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return '{}({}): {}'.format(self.__class__.__name__, self.pk, self.name)


class Variant(models.Model, VariantMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    display_name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=VariantMixin.SIZES)
    color = models.CharField(max_length=50, choices=VariantMixin.COLORS)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    class Meta:
        verbose_name = _('Variant')
        verbose_name_plural = _('Variants')

    def __str__(self):
        return '{}({}): {}'.format(self.__class__.__name__, self.pk, self.display_name)
