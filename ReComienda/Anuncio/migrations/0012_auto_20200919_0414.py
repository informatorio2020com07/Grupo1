# Generated by Django 3.1.1 on 2020-09-19 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Anuncio', '0011_anuncio_trans_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio_trans',
            name='permitir_comentarios',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contratista',
            name='permitir_comentarios',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Comentario_trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anuncio.anuncio_trans')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario_contra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anuncio.contratista')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
