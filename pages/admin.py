from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Page

class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_in_navigation')
    prepopulated_fields = {"slug": ("title", )}

# Register your models here.
admin.site.register(Page, PageAdmin)
