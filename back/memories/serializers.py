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
        fields = ['id', 'user', 'article_title', 'content', 'date', 'diary_img']

class ArticleUpdateSerializer(ArticleSerializer):
    class Meta:
        model = Article
        fields = ['id', 'user', 'article_title', 'content', 'date', 'diary_img']

class GenreDetailSerializer(GenreSerializer):
    item = ItemSerializer(many=True)
    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ['movie', ]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'todo_title']

class UserDetailSerializer(serializers.ModelSerializer):
    liked_items = ItemSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'liked_items', 'eng_name', 'pet_name', 'pet_img']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'liked_items', 'eng_name', 'pet_name', 'pet_img']