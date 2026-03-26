from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/add/', views.genre_add, name='genre_add'),
    path('genres/delete/<int:pk>/', views.genre_delete, name='genre_delete'),

    path('movies/', views.movie_list, name='movie_list'),
    path('movies/add/', views.movie_add, name='movie_add'),
    path('movies/delete/<int:pk>/', views.movie_delete, name='movie_delete'),
    path('genres/edit/<int:pk>/', views.genre_edit, name='genre_edit'),
    path('movies/edit/<int:pk>/', views.movie_edit, name='movie_edit'),
]