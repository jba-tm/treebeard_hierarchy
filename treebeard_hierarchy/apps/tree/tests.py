from django.test import TestCase

from .models import Category


class CategoryModelText(TestCase):
    def f(self, node_id):
        return Category.objects.get(pk=node_id)

    def test_add_category(self):
        get = lambda node_id: Category.objects.get(pk=node_id)
        print(get)
