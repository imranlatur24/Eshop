from django.contrib import admin
from .models.products import Prodcuts
from .models.category import Category
from .models.customers import Customer
from .models.orders import Orders


class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
admin.site.register(Prodcuts,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Orders)