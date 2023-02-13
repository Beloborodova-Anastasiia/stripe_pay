from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    """ Модель для еовара"""
    name = models.CharField(max_length=200)
    price = models.IntegerField(
        validators=(MinValueValidator(1),)
    )
    description = models.TextField()

    def __str__(self):
        """Вернуть поля title как строки"""
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
