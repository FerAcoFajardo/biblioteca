# Generated by Django 3.1.3 on 2020-11-17 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20201116_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.CreateModel(
            name='libre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libro.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
