from collections import Counter
from itertools import count
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models

# Register your models here.


admin.site.register(models.Collection)




#here is another way of customizing pruduct class 
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status']
    list_editable = ['price']  #what you can edit 
    list_per_page = 10    #how many can go on the page
    
    @admin.display(ordering= 'inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok' 
#admin.site.register(models.Product)

admin.site.register(models.Promotion)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 5
    ordering = ['first_name', 'last_name']
#admin.site.register(models.Customer)

admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Address)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
