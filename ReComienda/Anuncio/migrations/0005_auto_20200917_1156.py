# Generated by Django 3.1.1 on 2020-09-17 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anuncio', '0004_auto_20200916_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='transporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anuncio.transporte'),
        ),
    ]
