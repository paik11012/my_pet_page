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

```
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
```

