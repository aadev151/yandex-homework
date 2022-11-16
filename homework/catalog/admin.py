from django.contrib import admin

from .models import Category, Gallery, Image, Item, Tag


admin.site.site_header = ('Kitty Sneakers Admin')
admin.site.index_title = ''
admin.site.site_title = ('Admin Panel | Kitty Sneakers')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb', 'is_on_main')
    list_display_links = ('name',)
    list_editable = ('is_published', 'is_on_main',)
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb',)
