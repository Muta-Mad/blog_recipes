from django.db import models


class Recipe(models.Model):
    recipe = models.TextField(verbose_name='Рецепт', max_length=250, default='Рецепт')
    author = models.CharField(verbose_name='Автор', max_length=20,  default='Автор')

    def __str__(self):
        return self.recipe

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'