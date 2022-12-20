from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Order)
admin.site.register(Price)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Product_Category)
admin.site.register(Product_Stock)
admin.site.register(Discount)
admin.site.register(Product_Comment)
admin.site.register(Product_Like)
