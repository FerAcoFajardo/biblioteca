# Generated by Django 3.1.3 on 2020-11-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_auto_20201116_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_registro',
            field=models.DateField(auto_now=True, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_registro',
            field=models.DateField(auto_now=True, verbose_name='Fecha de registro'),
        ),
    ]
