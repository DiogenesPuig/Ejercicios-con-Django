# Generated by Django 2.2 on 2020-06-24 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_auto_20200624_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='Libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Libro'),
        ),
    ]
