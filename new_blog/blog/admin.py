from django.contrib import admin
from .models import Category,Blog

# Register your models here.
admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_at','updated_at']
# admin.site.register(Blog)