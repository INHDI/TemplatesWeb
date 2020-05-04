from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
   list_display = ('Ho_ten',)
admin.site.register(Cart, CartAdmin)