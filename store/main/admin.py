from django.contrib import admin
from main.models import Product, Category, SubCategory, Item
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)
