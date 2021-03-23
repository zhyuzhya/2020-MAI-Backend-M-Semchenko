from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименование")
    current_price = models.FloatField(verbose_name="Текущая стоимость")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
