
from django.urls import path
from .views import *

urlpatterns = [
    path('anime/', AnimeListView.as_view(), name='Anime'),
    path('anime/<int:pk>/', AnimeDetail.as_view(), name='Anime_Create')
]
