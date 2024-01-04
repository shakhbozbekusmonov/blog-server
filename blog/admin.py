from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog site admin'