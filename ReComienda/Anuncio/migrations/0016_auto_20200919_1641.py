# Generated by Django 3.1.1 on 2020-09-19 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Anuncio', '0015_auto_20200919_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratista',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
