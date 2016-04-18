# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroundType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'EC8 Soil classification',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='ground_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.GroundType', verbose_name='EC8 Soil classification'),
        ),
    ]