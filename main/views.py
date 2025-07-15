from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

class GeneralView(generics.ListAPIView):
    queryset = General.objects.all()
    serializer_class = GenerelSerializer

class GameView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class StartGameView(generics.ListAPIView):
    queryset = StartGame.objects.all()
    serializer_class = StartGameSerializer

class DowlandsView(generics.ListAPIView):
    queryset = Dowlands.objects.all()
    serializer_class = DowlandsSerializer

class StrategyView(generics.ListAPIView):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer

class ReviewsView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


def index(request):
    context = {
        'general': General.objects.first(),
        'games': Game.objects.all(),
        'start': StartGame.objects.all(),
        'downloads': Dowlands.objects.all(),
        'strategies': Strategy.objects.all(),
        'reviews': Reviews.objects.all(),
    }
    return render(request, 'index.html', context)