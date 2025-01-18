from django.db import models


class Recipe(models.Model):
    title = models.CharField('Название', max_length=20)
    recipes = models.TextField(verbose_name='Рецепт')
    author = models.CharField(verbose_name='Автор', max_length=20)
    img = models.ImageField(verbose_name='Изображение', upload_to='recipe_image', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
