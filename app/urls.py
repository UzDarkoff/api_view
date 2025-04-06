from django.urls import path
from . import views

urlpatterns = [
    # Movie
    path('movies/', views.movie_api, name='movie-api'),
    path('movies/<int:pk>/', views.movie_detail, name='movie-detail'),

    # Actor endpoints
    path('actors/', views.actor_api, name='actor-api'),
    path('actors/<int:pk>/', views.actor_detail, name='actor-detail'),
]
