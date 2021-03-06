# Generated by Django 2.2.5 on 2021-03-24 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producers', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('current_price', models.FloatField(verbose_name='Текущая стоимость')),
                ('year', models.IntegerField(null=True, verbose_name='Год выпуска')),
                ('color', models.CharField(max_length=64, null=True, verbose_name='Цвет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.Category')),
                ('producer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='producers.Producer')),
            ],
        ),
    ]
