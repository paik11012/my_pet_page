from django.contrib import admin
from .models import Article, User, Genre, Item, Todo
# Register your models here.
admin.site.register(Article)
admin.site.register(Genre)
admin.site.register(Item)
admin.site.register(Todo)
admin.site.register(User)