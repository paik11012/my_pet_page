from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class User(AbstractUser):
    eng_name = models.TextField(max_length=15)
    liked_items = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_users')
    pet_name = models.TextField(max_length=20)
    pet_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.eng_name

class Item(models.Model):
    genre = models.ForeignKey(Genre, related_name="item", on_delete=models.CASCADE)  
    item_title = models.CharField(max_length=20)
    item_img = models.ImageField(upload_to='images/')
    cost = models.TextField(max_length=20)
    brand = models.TextField(max_length=20)
    description = models.TextField(max_length=50)
    purchase_link = models.TextField(max_length=50)
    def __str__(self):
        return self.item_title

class Article(models.Model):
    title = models.TextField(max_length=20)
    date = models.DateField()
    def __str__(self):
        return self.title