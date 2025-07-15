from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "display_img")

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return "Нет фото"
    display_img.short_description = "фото"


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "display_img")

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px:" />', obj.img.url)
        return "Нет фото"
    display_img.short_description = "фото"


@admin.register(StartGame)
class StartGameAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "description")


@admin.register(Dowlands)
class DowlandsAdmin(admin.ModelAdmin):
    list_display = ("title", "display_img", "url")

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return "Нет фото"
    display_img.short_description = "фото"


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ("title", "junior", "middle", "pro")


@admin.register(Reviews)
class ReviewaAdmin(admin.ModelAdmin):
    list_display = ("name", "text")

