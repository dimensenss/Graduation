from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from clients.models import Client
from services.models import Category

admin.site.register(Client)



class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)