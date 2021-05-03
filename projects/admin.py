from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Project, Credit, Asset

class CreditAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('role', 'name')
    model = Credit

class AssetAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('caption', 'image')
    model = Asset

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'url', 'is_visible')
    prepopulated_fields = {"slug":("title", )}
    inlines = [
        CreditAdmin,
        AssetAdmin
    ]

# Register your models here.
admin.site.register(Project, ProjectAdmin)
