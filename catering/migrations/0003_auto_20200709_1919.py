# Generated by Django 3.0.8 on 2020-07-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0002_auto_20200708_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название'),
        ),
    ]