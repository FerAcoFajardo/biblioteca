# Generated by Django 3.1.3 on 2020-11-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0008_auto_20201116_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]
