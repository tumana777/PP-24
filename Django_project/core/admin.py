from django.contrib import admin
from .models import Car, Category

admin.site.register([Car, Category])