from django.contrib import admin
from blog.models import Blog, BlogStat

class BlogAdmin(admin.ModelAdmin):
    list_display = ['created_at','blog_category','blog_title','blog_des']

class BlogStatAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'comments', 'like', 'dislike']

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogStat, BlogStatAdmin)


