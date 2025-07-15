from rest_framework import serializers
from .models import *


class GenerelSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class StartGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartGame
        fields = "__all__"

class DowlandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dowlands
        fields = "__all__"

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = "__all__"

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"