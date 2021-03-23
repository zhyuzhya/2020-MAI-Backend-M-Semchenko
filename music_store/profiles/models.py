from django.db import models

# Create your models here.
class Profile(models.Model):
    login = models.CharField(max_length=32, verbose_name="login", null=False, blank=False)
    first_name = models.CharField(max_length=64, verbose_name="Имя", null=True, blank=True)
    second_name = models.CharField(max_length=128, verbose_name="Фамилия", null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    email_address = models.EmailField(verbose_name="Адрес эл. почты", null=False, blank=False)
    password = models.CharField(max_length=32, verbose_name="Пароль", null=False, blank=False)
