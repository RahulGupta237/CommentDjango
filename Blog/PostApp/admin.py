from django.contrib import admin
from .models import Post,Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display =  ('title', 'category', 'author', 'description', 'publish')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)


