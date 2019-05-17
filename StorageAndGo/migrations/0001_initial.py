# Generated by Django 2.1.7 on 2019-05-03 07:41

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('qty', models.IntegerField(null=True)),
                ('tempMinDegree', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(-30), django.core.validators.MaxValueValidator(30)])),
                ('tempMaxDegree', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(-30), django.core.validators.MaxValueValidator(30)])),
                ('humidMin', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('humidMax', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('sla', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manifesto',
            fields=[
                ('ref', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('creationDate', models.DateTimeField(default=datetime.date.today)),
                ('revisionDate', models.DateTimeField(null=True)),
                ('withdrawal', models.BooleanField(null=True)),
                ('totalpackets', models.IntegerField(null=True)),
                ('fromLocation', models.CharField(max_length=255)),
                ('toLocation', models.CharField(max_length=255)),
                ('Products', models.ManyToManyField(related_name='Products', to='StorageAndGo.Contenidor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('temperatureMin', models.IntegerField(default=0)),
                ('temperatureMax', models.IntegerField(default=0)),
                ('humitMin', models.IntegerField(default=0)),
                ('humitMax', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
                ('contenidorsInside', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('accepted', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('hight_priority', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Avaria',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='StorageAndGo.Task')),
                ('object', models.TextField(blank=True, default='')),
                ('room', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='StorageAndGo.Room')),
            ],
            bases=('StorageAndGo.task',),
        ),
        migrations.CreateModel(
            name='TaskMaintenance',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='StorageAndGo.Task')),
                ('temperature', models.IntegerField(blank=True, default=0)),
                ('room', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='StorageAndGo.Room')),
            ],
            bases=('StorageAndGo.task',),
        ),
        migrations.CreateModel(
            name='TaskOperator',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='StorageAndGo.Task')),
                ('product', models.TextField(blank=True, default='')),
                ('quantity', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='destination', to='StorageAndGo.Room')),
                ('origin', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='origin', to='StorageAndGo.Room')),
            ],
            bases=('StorageAndGo.task',),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_maintenance', to=settings.AUTH_USER_MODEL),
        ),
    ]