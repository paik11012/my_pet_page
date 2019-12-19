from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import ItemSerializer, GenreDetailSerializer, GenreSerializer, ArticleSerializer, ArticleUpdateSerializer, UserSerializer, UserDetailSerializer, TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo, Genre, Item, Article
import requests
User = get_user_model

@api_view(['POST'])
def todo_create(request):
    # request.data는 axios의 body로 전달한 데이터
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)


@api_view(['DELETE'])
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=204)

@api_view(['GET'])
def itemlist(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items)
    return Response(serializer.data)

@api_view(['GET'])
def genrelist(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genredetail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    if request.method == 'GET':
        serializer = GenreDetailSerializer(genre, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def articlelist(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def articledetail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)  # many같은것 모르겠음
        return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = ArticleUpdateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'PUT':
        serializer = ArticleUpdateSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # delete면
        article.delete()
        return Response({'message':'글'})


def userdetail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)
