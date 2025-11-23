from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("admin/css/ckeditor_force_black.css",)}

    
    readonly_fields = ["author"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)
