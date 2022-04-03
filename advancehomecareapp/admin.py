from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'phone', 'date_time')


admin.site.register(Customer, CustomerAdmin)