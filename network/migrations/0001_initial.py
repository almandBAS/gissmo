# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0001_firstone'),
        ('document', '0001_initial'),
        ('place', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('affiliation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_historical_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='StationXML Historical code')),
                ('xml_alternate_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='StationXML Alternate code')),
                ('xml_restricted_status', models.IntegerField(blank=True, choices=[(0, 'Open'), (1, 'Closed'), (2, 'Partial')], null=True, verbose_name='StationXML Restricted status')),
                ('code', models.IntegerField(choices=[(0, 'HHE'), (1, 'HHN'), (2, 'HHZ'), (3, 'BHE'), (4, 'BHN'), (5, 'BHZ'), (6, 'LHE'), (7, 'LHN'), (8, 'LHZ'), (9, 'HNE'), (10, 'HNN'), (11, 'HNZ'), (12, 'DPE'), (13, 'DPN'), (14, 'DPZ'), (15, 'CHE'), (16, 'CHN'), (17, 'CHZ'), (18, 'EHE'), (19, 'EHN'), (20, 'EHZ'), (21, 'ELE'), (22, 'ELN'), (23, 'ELZ'), (24, 'SHE'), (25, 'SHN'), (26, 'SHZ'), (27, 'MHE'), (28, 'MHN'), (29, 'MHZ'), (30, 'VHE'), (31, 'VHN'), (32, 'VHZ'), (33, 'UHE'), (34, 'UHN'), (35, 'UHZ'), (36, 'LDI'), (37, 'LII'), (38, 'LKI'), (39, 'BH1'), (40, 'BH2'), (41, 'LH1'), (42, 'LH2'), (43, 'VH1'), (44, 'VH2'), (45, 'HN2'), (46, 'HN3')])),
                ('location_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='Location code')),
                ('azimuth', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Azimuth (°)')),
                ('dip', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='DIP (°)')),
                ('sample_rate', models.FloatField(verbose_name='Sample rate (Samples/S)')),
                ('start', models.DateTimeField(verbose_name='Starting date')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Ending date')),
                ('description', models.TextField(blank=True, null=True)),
                ('calibration_unit', models.IntegerField(blank=True, choices=[(0, 'Displacement in meters'), (1, 'Velocity in meters per second'), (2, 'Acceleration in meters per second squared')], null=True, verbose_name='Calibration unit')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitude (°)')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitude (°)')),
                ('elevation', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, verbose_name='Elevation (m)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Datatype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.IntegerField(choices=[(0, 'Sensor'), (1, 'Preamplifier'), (2, 'Datalogger'), (3, 'Equipment'), (4, 'Other 1'), (5, 'Other 2'), (6, 'Other 3'), (7, 'Other 4'), (8, 'Other 5')], verbose_name='Type')),
                ('start', models.DateTimeField(auto_now=True, verbose_name='Starting date')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Ending date')),
                ('depth', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Depth (m)')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitude (°)')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitude (°)')),
                ('elevation', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, verbose_name='Elevation (m)')),
                ('configurations', models.ManyToManyField(blank=True, to='equipment.Configuration')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.Installation', verbose_name='Connected to')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_historical_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='StationXML Historical code')),
                ('xml_alternate_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='StationXML Alternate code')),
                ('xml_restricted_status', models.IntegerField(blank=True, choices=[(0, 'Open'), (1, 'Closed'), (2, 'Partial')], null=True, verbose_name='StationXML Restricted status')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='Starting date')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Ending date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_historical_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='StationXML Historical code')),
                ('xml_alternate_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='StationXML Alternate code')),
                ('xml_restricted_status', models.IntegerField(blank=True, choices=[(0, 'Open'), (1, 'Closed'), (2, 'Partial')], null=True, verbose_name='StationXML Restricted status')),
                ('code', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.IntegerField(choices=[(0, 'Theoritical'), (1, 'Test'), (2, 'Production')], default=0)),
                ('documents', models.ManyToManyField(blank=True, to='document.Document')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiliation.Organism')),
                ('elevation', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, verbose_name='Elevation (m)')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitude (°)')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitude (°)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='channel',
            name='datatypes',
            field=models.ManyToManyField(blank=True, to='network.Datatype'),
        ),
        migrations.AddField(
            model_name='channel',
            name='installation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.Installation'),
        ),
        migrations.AddField(
            model_name='channel',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.Network'),
        ),
        migrations.AddField(
            model_name='channel',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.Station'),
        ),
        migrations.AddField(
            model_name='channel',
            name='configurations',
            field=models.ManyToManyField(blank=True, to='equipment.Configuration'),
        ),
        migrations.CreateModel(
            name='Built',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
            ],
        ),
        migrations.AddField(
            model_name='built',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.Station'),
        ),
        migrations.AddField(
            model_name='station',
            name='places',
            field=models.ManyToManyField(through='network.Built', to='place.Place'),
        ),
    ]
