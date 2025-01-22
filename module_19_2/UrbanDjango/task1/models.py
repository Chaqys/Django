from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Buyer(models.Model):
    name = models.CharField(max_length=255)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Баланс
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Game(models.Model):
    title = models.CharField(max_length=255)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Размер файлов игры
    description = models.TextField()  # Описание игры
    age_limited = models.BooleanField(default=False)  # Ограничение по возрасту
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def add_buyer(self, buyer):
        if self.age_limited and buyer.age < 18:
            raise ValidationError(f"Покупатели младше 18 лет не могут приобретать игры с возрастными ограничениями.")
        self.buyers.add(buyer)