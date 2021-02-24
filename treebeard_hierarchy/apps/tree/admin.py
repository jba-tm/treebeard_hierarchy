from django.contrib import admin

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import MaterializedCategory, MaterializedProduct, NestedCategory, NestedProduct


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(MaterializedCategory)


class NestedCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(NestedCategory)


admin.site.register(MaterializedCategory, CategoryAdmin)
admin.site.register(NestedCategory, NestedCategoryAdmin)
admin.site.register(MaterializedProduct, admin.ModelAdmin)
admin.site.register(NestedProduct, admin.ModelAdmin)
