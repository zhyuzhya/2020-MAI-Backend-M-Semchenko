from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название категории")

    def __str__(self):
        return f"{self.name}"
