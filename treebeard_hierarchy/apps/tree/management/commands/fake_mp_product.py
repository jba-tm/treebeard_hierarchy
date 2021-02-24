

max_id = Category.objects.all().aggregate(max_id=Max("id"))['max_id']
   ...:     pk = random.randint(1, max_id)
   ...:     return Category.objects.get(pk=pk)