from django.contrib import admin
from markdownx.admin import MarkdownModelAdmin
from .models import Post, Category, Tag

admin.site.register(Post, MarkdownModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepipukated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
