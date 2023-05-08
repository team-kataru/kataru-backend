from django.urls import path
from . import views

urlpatterns = [
    # path('', views.kataru_api, name='kataru_api'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('genres/', views.genres, name='genres'),
    path('genres/<int:pk>/', views.genres_id, name='genres_id'),
    path('genres/<int:pk>/update/', views.genres_id, name='genres_id_update'),
    path('genres/<int:pk>/delete/', views.genres_id, name='genres_id_delete'),
    path('prompts/', views.prompts, name='prompts'),
    path('users/', views.users, name='users'),
    path('users/<int:pk>/', views.users_id, name='users_id'),
    path('users/<int:pk>/update/', views.users_id, name='users_id_update'), 
    path('users/<int:pk>/delete/', views.users_id, name='users_id_delete')
]