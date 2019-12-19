from django.urls import path, include
from . import views

urlpatterns = [
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
    
]