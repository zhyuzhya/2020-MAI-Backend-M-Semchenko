from django.db import models
from categories.models import Category
from producers.models import Producer

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименование", null=False, blank=False)
    current_price = models.FloatField(verbose_name="Текущая стоимость")
    year = models.IntegerField(verbose_name="Год выпуска", null=True)
    color = models.CharField(max_length=64, verbose_name="Цвет", null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.producer} {self.name}"
