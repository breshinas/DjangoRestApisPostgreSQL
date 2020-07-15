from django.db import models
from django.contrib.auth.models import User

# Рецепт
class Recipe(models.Model):
    name = models.CharField(
        "Название",
        max_length=250,
        blank=False,
        default='')
    #ссылка на картинку
    url = models.URLField(
        "URL картинки",
        default='',
        blank=True,
        help_text="Ссылка на картинку")
    amount = models.DecimalField(
        "Цена",
        max_digits=15,
        decimal_places=2,
        default=1)

    # def __str__(self):
    #     return '[%s] %s %s' % (self.id, self.name, self.amount)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

# Заказ
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        help_text="Оператор заказа")
    customer = models.CharField(
        max_length=200,
        blank=False,
        default='',
        help_text="заказчик")
    # ==== итоги
    totalDishes = models.IntegerField(blank=False, default=1,
        help_text="Итого. Кол-во блюд")
    totalCount = models.IntegerField(blank=False, default=1,
        help_text="Итого. Кол-во позиций")
    totalAmount = models.DecimalField(max_digits=15, decimal_places=2, default=0,
        help_text="Итого. Сумма")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

# Заказанные блюда. Блюдо
class Dish(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE)
    # TODO: user
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        help_text="Оператор заказа")
    recipe = models.ForeignKey(
        Recipe, 
        on_delete = models.CASCADE)
    count = models.IntegerField(
        default=1,
        help_text="Количество позиций")
    amount = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0,
        help_text="Сумма за позицию")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
