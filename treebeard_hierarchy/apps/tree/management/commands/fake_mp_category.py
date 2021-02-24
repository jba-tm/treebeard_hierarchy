from django.core.management.base import BaseCommand
from treebeard_hierarchy.apps.tree.models import MaterializedCategory
from faker import Faker


class Command(BaseCommand):
    help = 'Create fake categories'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--total', type=int, default=1,
                            help='Indicates the number of categories to be created')

    def handle(self, *args, **kwargs):
        total = kwargs.get('total', 1)
        faker = Faker()

        for i in range(1, total+1):
            prefix = faker.word()
            category = MaterializedCategory.add_root(title=f'{prefix.capitalize()} {i}')
            self.stdout.write(f'Root category created with name: {category}')
            for j in range(1, total+1):
                child = category.add_child(title=f'{prefix} {i}.{j}')
                self.stdout.write(f'Category created with name: {child}')

                for n in range(1, total+1):
                    child_child = child.add_child(title=f'{prefix} {i}.{j}.{n}')
                    self.stdout.write(f'Category created with name: {child_child}')
