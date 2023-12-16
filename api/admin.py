from django.contrib import admin
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display=["company_name","country_name","price","mileage","fuel_type"]
    
admin.site.register(Car,CarAdmin)