from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название', help_text='Уникальное название обёртки, не более 256 символов')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(default=100,
                                                   verbose_name='Порядок отображения')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название', help_text='Уникальное название обёртки, не более 256 символов')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название', help_text='Уникальное название обёртки, не более 256 символов')
    class Meta:
        verbose_name = 'объект «Обёртка»'
        verbose_name_plural = 'Обёртки'


class IceCream(PublishedModel):
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')
    title = models.CharField(max_length=256, verbose_name='Название', help_text='Уникальное название обёртки, не более 256 символов')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинги')
    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title