# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 12:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('affiliation', '0001_initial'),
        ('place', '0001_initial'),
        ('document', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('start', models.DateTimeField(auto_now=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Serial number')),
                ('vendor', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase date')),
                ('clock_drift', models.FloatField(blank=True, null=True, verbose_name='Clock drift')),
                ('clock_drift_unit', models.CharField(blank=True, default='SECONDS/SAMPLE', max_length=15, null=True)),
                ('storage_format', models.CharField(blank=True, max_length=50, null=True, verbose_name='Storage format')),
                ('note', models.TextField(blank=True, null=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(blank=True, to='document.Document')),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenEquipmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Forbidden Model',
            },
        ),
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255, verbose_name='IP Address')),
                ('netmask', models.GenericIPAddressField(verbose_name='Netmask')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rank', models.IntegerField()),
                ('manufacturer', models.CharField(default='Unknown', max_length=50)),
                ('chain_type', models.IntegerField(choices=[(0, 'Sensor'), (1, 'Preamplifier'), (2, 'Datalogger'), (3, 'Equipment'), (4, 'Other 1'), (5, 'Other 2'), (6, 'Other 3'), (7, 'Other 4'), (8, 'Other 5')], null=True, verbose_name='Acquisition chain type')),
                ('is_network_model', models.BooleanField(default=False, verbose_name='Network configurable?')),
            ],
            options={
                'verbose_name': 'Model',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Model')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.IntegerField(choices=[(0, 'SSH protocol'), (1, 'Seed link protocol'), (2, 'HTTP'), (3, 'HTTPS'), (4, 'SNMP'), (5, 'ICMP')])),
                ('port', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(choices=[(0, 'Unknown'), (1, 'New'), (2, 'To be test'), (3, 'Available'), (4, 'Running'), (5, 'Failure'), (6, 'Broken'), (7, 'Waste'), (8, 'In transit'), (9, 'Spare part'), (10, 'Lost')], default=0)),
                ('start', models.DateTimeField(auto_now=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_equipment', to='equipment.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('rank', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.Type', verbose_name='Supertype')),
            ],
            options={
                'verbose_name': 'Type',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_default', models.BooleanField(default=False)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Parameter')),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Type', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='model',
            name='documents',
            field=models.ManyToManyField(blank=True, to='document.Document'),
        ),
        migrations.AddField(
            model_name='forbiddenequipmentmodel',
            name='original',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='equipment.Model', verbose_name='Forbidden Model'),
        ),
        migrations.AddField(
            model_name='forbiddenequipmentmodel',
            name='recommended',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommended_model', to='equipment.Model', verbose_name='Recommended Model'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Model'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiliation.Agency'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_place', to='place.Place'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_state', to='equipment.State'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment'),
        ),
    ]
