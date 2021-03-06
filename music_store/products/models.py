from django.db import models
from categories.models import Category
from producers.models import Producer

def get_picture_path(instance, filename):
    return f"pictures/{instance.producer}_{instance.name}_{filename}"

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименование", null=False, blank=False)
    current_price = models.FloatField(verbose_name="Текущая стоимость")
    year = models.IntegerField(verbose_name="Год выпуска", null=True)
    color = models.CharField(max_length=64, verbose_name="Цвет", null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT, null=True)
    picture = models.ImageField('Фотография', null=True, blank=True, upload_to=get_picture_path)

    def __str__(self):
        return f"{self.producer} {self.name}"

    def get_absolute_url(self):
        return f"/api/products/{self.id}/"
