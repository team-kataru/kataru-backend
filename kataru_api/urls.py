from django.urls import path
from . import views

urlpatterns = [
    # path('', views.kataru_api, name='kataru_api'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('genres/', views.genres, name='genres'),
    path('prompts/', views.prompts, name='prompts')
]