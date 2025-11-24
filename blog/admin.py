from django.contrib import admin
from .models import Blog,Comment

class CommentInline(admin.TabularInline):
    model=Comment
    extra=1
    fields=['comment']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines=[CommentInline]

    class Media:
        css = {"all": ("admin/css/ckeditor_force_black.css",)}
    
    readonly_fields = ["author"]

    def save_formset(self, request, form, formset, change):
        instances=formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.user=request.user
            instance.save()
        return super().save_formset(request, form, formset, change)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)
