from django.contrib import admin
from apps.product.models import Product, ProductFrom, ProductDetail


# Register your models here.
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductFrom)
