from django.contrib import admin
from .models import information
# Register your models here.


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'phone')


admin.site.register(information, PersonalInfoAdmin)

