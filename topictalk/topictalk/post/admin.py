from django.contrib import admin

from topictalk.post.models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass