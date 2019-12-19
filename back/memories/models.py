from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Genre(models.Model):  # 물건 종류, 장르 별 구분하기 위해 만듬
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class User(AbstractUser):
    eng_name = models.TextField(max_length=15)
    liked_items = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_users')
    pet_name = models.TextField(max_length=20)
    pet_img = models.ImageField(upload_to='images/pets')
    def __str__(self):
        return self.eng_name

class Item(models.Model): # 추천하는 물건 하나하나
    genre = models.ForeignKey(Genre, related_name="item", on_delete=models.CASCADE)  
    item_title = models.CharField(max_length=20)
    item_img = models.ImageField(upload_to='images/items/')
    cost = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    purchase_link = models.CharField(max_length=50)
    liked_users = models.ManyToManyField(User, related_name='liked_item', blank=True)
    def __str__(self):
        return self.item_title

class Article(models.Model):  # 유저가 쓰는 글
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    article_title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    date = models.DateField()
    diary_img = models.ImageField(upload_to='images/articles/')
    def __str__(self):
        return self.article_title

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_title = models.CharField(max_length=50)
    def __str__(self):
        return self.todo_title