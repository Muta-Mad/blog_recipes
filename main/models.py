from django.db import models


class Recipe(models.Model):
    title = models.CharField('Название', max_length=20)
    recipes = models.TextField(verbose_name='Рецепт', max_length=250)
    author = models.CharField(verbose_name='Автор', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'