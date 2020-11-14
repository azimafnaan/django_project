from django.contrib import admin

# Register your models here.
from .models import Friends,Products,Category
admin.site.register(Friends)
admin.site.register(Products)
admin.site.register(Category)
