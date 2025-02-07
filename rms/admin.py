from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name',)
   search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'category')
   list_filter = ('category',)
   search_fields = ('name','category__name')

class TableAdmin(admin.ModelAdmin):
   list_display = ('number', 'is_available')
   list_filter = ('is_available',)

class OrderItemInline(admin.TabularInline):
   model = OrderItem
class OrderAdmin(admin.ModelAdmin):
   list_display=('user','total_price','status','payment')
   list_filter = ('status','payment')
   inlines = (OrderItemInline,)
   # inline = [OrderItemInline]

admin.site.register(Food,FoodAdmin)
admin.site.register(Order,OrderAdmin)
# admin.site.register(OrderItem)
admin.site.register(Table,TableAdmin)