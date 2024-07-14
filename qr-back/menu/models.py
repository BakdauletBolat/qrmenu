from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    address = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='stores/', null=True, blank=True, verbose_name='Фотка')
    params = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Category(models.Model):
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name='Фотка')
    order = models.IntegerField(default=1, verbose_name='Сортировка')
    title = models.CharField(max_length=255, verbose_name='Названия')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='categories', verbose_name='Магазин')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']

    def __str__(self) -> str:
        return self.title


class Food(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='foods')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')
    discount_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8 , verbose_name='Цена со скидкой')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюды'

    def __str__(self) -> str:
        return self.name


class FoodImage(models.Model):
    image = models.ImageField(upload_to='goods/', verbose_name='Фотка')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо', related_name='images')

    class Meta:
        verbose_name = 'Фотки'
        verbose_name_plural = 'Фотки'