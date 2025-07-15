from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .views import *
from .import views 

schema_view = get_schema_view(
    openapi.Info( 
        title="Mines.ru",
        default_version='v1',
        description="Документация API для Мали",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("general", GeneralView.as_view()),
    path("game", GameView.as_view()),
    path("start_game", StartGameView.as_view()),
    path("dowlands", DowlandsView.as_view()),
    path("strategy", StrategyView.as_view()),
    path("reviews", ReviewsView.as_view()),

    path('', views.index, name='index'),
    path("api/malya/mines.ru/1win/api/documentation", schema_view.with_ui('swagger', cache_timeout=0)),
]