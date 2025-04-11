from django.contrib import admin
from .models import Blog , Category  , Comments
# Register your models here.


# admin.site.register(Blog)
admin.site.register(Category)

# admin.site.register(Comments)


class BlogAdmin(admin.ModelAdmin):
    list_display =('title','created_at','author')
    list_filter = ("created_at",)
    search_fields=("title",)
    ordering=("title",)
    date_hierarchy=("created_at")

admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'message',  'date', 'blog']
    readonly_fields = ( 'name',  'email', 'message',  'date' , 'blog')
    
admin.site.register(Comments , CommentAdmin)