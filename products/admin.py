from django.contrib import admin
from products.models.depart import Department
from products.models.item import Item

# Register your models here.

admin.site.register(Department)
admin.site.register(Item)
# admin.site.register(ProductImage)
