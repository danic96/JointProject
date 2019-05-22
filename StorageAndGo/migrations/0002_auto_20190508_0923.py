# Generated by Django 2.1.7 on 2019-05-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StorageAndGo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(default=0, verbose_name='Capacidad'),
        ),
        migrations.AlterField(
            model_name='room',
            name='contenidorsInside',
            field=models.IntegerField(default=0, verbose_name='Contenedores Dentro'),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='room',
            name='humitMax',
            field=models.IntegerField(default=0, verbose_name='Humedad MAX'),
        ),
        migrations.AlterField(
            model_name='room',
            name='humitMin',
            field=models.IntegerField(default=0, verbose_name='Humedad MIN'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='room',
            name='temperatureMax',
            field=models.IntegerField(default=0, verbose_name='Temperatura MAX'),
        ),
        migrations.AlterField(
            model_name='room',
            name='temperatureMin',
            field=models.IntegerField(default=0, verbose_name='Temperatura MIN'),
        ),
    ]
