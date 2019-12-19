# My Pet Page

### 1. 팀 정보

| 팀원   | 업무 내용                                      |
| ------ | ---------------------------------------------- |
| 백민주 | Django 모델 구성, 데이터 수집 및 관리(API이용) |

도움을 준 사람: 공정배(readme 작성)

### 2. 데이터베이스 모델링(ERD)

draw.io



# 본격 프로젝트 시작



## 1. 가상환경 설정

front, back폴더 만들고 back폴더에서

```
python -m venv venv  # 가상환경 만들기
source venv/Scripts/activate  # 가상환경 잡기
```

```
pip list
pip install django
```

## 2. Django Modeling

MTV 모델 이용하는 장고(model, template, view)

```
$ django-admin startproject lovelyfriends .
$ python manage.py startapp memories
```

프로젝트랑 앱 시작, 기본 셋팅하기

models.py

```python
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
        return self.id

class Item(models.Model): # 추천하는 물건
    genre = models.ForeignKey(Genre, related_name="item", on_delete=models.CASCADE)  
    item_title = models.CharField(max_length=20)
    item_img = models.ImageField(upload_to='images/items/')
    cost = models.TextField(max_length=20)
    brand = models.TextField(max_length=20)
    description = models.TextField(max_length=50)
    purchase_link = models.TextField(max_length=50)
    def __str__(self):
        return self.item_title

class Article(models.Model):  # 유저가 쓰는 글
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.TextField(max_length=20)
    content = models.TextField(max_length=100)
    date = models.DateField()
    diary_img = models.ImageField(upload_to='images/articles/')
    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
```

serializer.py

```python
from rest_framework import serializers
from .models import Genre, Article, Item, User, Todo
from django.contrib.auth import get_user_model
User = get_user_model

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'genre', 'item_title', 'item_img', 'cost', 'brand', 'description', 'purchase_link', 'liked_users']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'content', 'date', 'diary_img']

class ArticleUpdateSerializer(ArticleSerializer):
    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'content', 'date', 'diary_img']

class GenreDetailSerializer(GenreSerializer):
    item = ItemSerializer(many=True)
    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ['movie', ]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title']

class UserDetailSerializer(serializers.ModelSerializer):
    liked_items = ItemSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'liked_items', 'eng_name', 'pet_name', 'pet_img']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'liked_items', 'eng_name', 'pet_name', 'pet_img']
```

admin.py에 등록해서 django admin으로 관리할 수 있도록 설정

urls.py

```python
	# todo관련
    path('todos/', views.todo_create),
    path('todos/<int:todo_id>/', views.todo_delete),
    # item관련(수정, 삭제는 나아중에 추가)
    path('itemlist/', views.itemlist),
    path('genrelist/', views.genrelist),
    path('genredetail/<int:genre_pk>/', views.genredetail),
    # article관련
    path('articlelist', views.articlelist),
    path('articledetail/<int:article_pk>/', views.articledetail),
    path('create/', views.create),
    path('update/<int:article_pk>/', views.update),
    # user관련
    path('userdetail/<int:user_pk>/', views.userdetail),
```
views.py 설정



## 3. FRONT 만들기

```

```

