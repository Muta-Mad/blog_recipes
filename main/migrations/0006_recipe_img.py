# Generated by Django 3.2.16 on 2025-01-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_recipe_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.ImageField(blank=True, upload_to='recipe_image', verbose_name='Изображение'),
        ),
    ]