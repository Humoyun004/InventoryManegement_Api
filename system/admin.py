from django.contrib import admin
from .models import Product, Part, Order


admin.site.register(Product)
admin.site.register(Part)
admin.site.register(Order)