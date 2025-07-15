from django.db import models

class General(models.Model):
    title = models.CharField(max_length=250, verbose_name="Загаловок")
    description = models.TextField(verbose_name="Описания")
    information = models.TextField(verbose_name="Информация")
    url = models.URLField(verbose_name="Ссфлка на бота")
    img = models.ImageField(upload_to="general/img", verbose_name="Изображения")

    class Meta:
        verbose_name = "Главная информация"
        verbose_name_plural = "Главная информация"


class Game(models.Model):
    img = models.ImageField(upload_to="game/img", verbose_name="Иконка")
    title = models.CharField(max_length=250, verbose_name="Описание")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "ИГРА MINES ЭТО"
        verbose_name_plural = "ИГРА MINES ЭТО"


class StartGame(models.Model):
    number = models.IntegerField(verbose_name="Номерация")
    title = models.CharField(max_length=250, verbose_name="Описание")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "КАК НАЧАТЬ ИГРАТЬ"
        verbose_name_plural = "КАК НАЧАТЬ ИГРАТЬ"


class Dowlands(models.Model):
    img = models.ImageField(upload_to="dowlands/img", verbose_name="Картинка")
    url = models.URLField(verbose_name="Ссылка на бота")
    title = models.CharField(max_length=2500, verbose_name="Загаловок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "СКАЧАТЬ MINES"
        verbose_name_plural = "СКАЧАТЬ MINES"


class Strategy(models.Model):
    title = models.CharField(max_length=250, verbose_name="Загаловок")
    junior = models.TextField(verbose_name="Стратегия для новичка")
    middle = models.TextField(verbose_name="Стратегия для среднего игрока")
    pro = models.TextField(verbose_name="Стратегия для профессионала")

    class Meta:
        verbose_name = "СТРАТЕГИИ ВЫИГРЫША В MINES"
        verbose_name_plural = "СТРАТЕГИИ ВЫИГРЫША В MINES"


class Reviews(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name="Дата отзыва", null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name="Имя")
    text = models.TextField(verbose_name="Отзыв")

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"