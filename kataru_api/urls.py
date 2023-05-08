from django.urls import path
from . import views

urlpatterns = [
    # path('', views.kataru_api, name='kataru_api'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('genres/', views.genres, name='genres'),
    path('genres/<int:pk>/', views.genres_id, name='genres_id'),
    path('prompts/', views.prompts, name='prompts'),
    path('prompts/<int:pk>/', views.prompts_id, name='prompts_id'),
    path('users/', views.users, name='users'),
    path('users/<int:pk>/', views.users_id, name='users_id'),
]