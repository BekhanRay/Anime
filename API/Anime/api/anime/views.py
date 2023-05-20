from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Anime
from .serializers import AnimeSerializer


class AnimeListView(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAuthenticated,)


class AnimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
