from django.db import models

# Create your models here.

class Producer(models.Model):
    name = models.CharField(max_length=64, verbose_name="Наименование", null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
