from django.contrib import admin
from .models import Product

#oluşturulan product app'i site olarak admin içerisine eklendi
admin.site.register(Product)
