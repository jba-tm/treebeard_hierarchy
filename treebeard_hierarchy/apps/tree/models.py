from django.db import models
from django.utils.translation import gettext_lazy as _

from treebeard.mp_tree import MP_Node
from treebeard.ns_tree import NS_Node


class HierarchyMixin:
    def __str__(self):
        full_path = [self.title]
        k = self.get_parent()
        while k is not None:
            full_path.append(k.title)
            k = k.get_parent()
        return ' -> '.join(full_path[::-1])


class MaterializedCategory(HierarchyMixin, MP_Node):
    title = models.CharField(max_length=50, unique=True)

    node_order_by = ['title']

    class Meta:
        verbose_name_plural = _('Materialized categories')
        verbose_name = _('Materialized category')


class MaterializedProduct(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(MaterializedCategory, verbose_name=_('Category'), related_name='category_ideas',
                                 on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class NestedCategory(HierarchyMixin, NS_Node):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = _('Nested categories')
        verbose_name = _('Nested category')


class NestedProduct(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(NestedCategory, verbose_name=_('Category'),
                                 related_name='nested_category_nested_product', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
