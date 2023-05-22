from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_text', 'created_by', 'created_at','updated_at')

admin.site.register(Comment,CommentAdmin)