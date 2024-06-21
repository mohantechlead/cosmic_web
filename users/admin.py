from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(customer_profile)
admin.site.register(supplier_profile)
