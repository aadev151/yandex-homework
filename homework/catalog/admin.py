from django.contrib import admin

from .models import Category, Item, Tag


admin.site.site_header = ('SuperSneakers Admin')
admin.site.index_title = ''
admin.site.site_title = ('Admin Panel | SuperSneakers')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb',)
    list_display_links = ('name',)
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
