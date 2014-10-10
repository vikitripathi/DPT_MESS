from django.contrib import admin
from reviewSystem.models import Item,Category,User,Rating

# register your model here
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Rating)
#the above method is an inefficient method  to show  data from two related tables