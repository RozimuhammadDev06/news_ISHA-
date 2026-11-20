from django.contrib import admin
from .models import Category, New, NewImage, Comment, Contact, Subscribe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name', 'slug', 'is_menu', 'get_menu_status')
    list_display_links = ('id', 'cat_name')
    search_fields = ('cat_name',)
    list_filter = ('is_menu',)
    list_editable = ('slug',)
   
    @admin.display(description="menudagi status")
    def get_menu_status(self, obj):
        return "menu" if obj.is_menu else "yopish"


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'views', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'short_dest', 'description', 'tegs')
    list_filter = ('category', 'created_at')
    readonly_fields = ('created_at',) 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'new', 'is_sub', 'created_at')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'massage')
    list_filter = ('is_sub', 'created_at', 'new')
    readonly_fields = ('created_at',)
    


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'is_contacted', 'is_trash')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'phone', 'message')
    list_filter = ('is_contacted', 'is_trash')
    list_editable = ('is_contacted', 'is_trash')

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'created_at')
    list_display_links = ('id', 'email')
    search_fields = ('email',)
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active',)
