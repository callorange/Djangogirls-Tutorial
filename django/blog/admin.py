from django.contrib import admin

from .models import Post, PostTrash

admin.site.register(Post)
admin.site.register(PostTrash)