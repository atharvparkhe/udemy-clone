from django.contrib import admin
from .models import *


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['owner', 'is_paid', 'coupon_applied', 'total_price']
    
admin.site.register(OrderModel,OrderModelAdmin)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['item','quantity','total']

admin.site.register(OrderItemsModel, OrderItemsAdmin)

class CouponsAdmin(admin.ModelAdmin):
    list_display = ["coupon_name", "use_times", "coupon_discount_amount", "is_active"]

admin.site.register(Coupons, CouponsAdmin)
