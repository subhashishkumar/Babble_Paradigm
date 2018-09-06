# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 07:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InputForms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accd_details',
            fields=[
                ('accd_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Accident ID')),
                ('accd_type', models.CharField(choices=[('Fatal', 'Fatal'), ('Reportable', 'Reportable'), ('Non-Reportable', 'Non-Reportable'), ('First-Aid', 'First-Aid')], default='Fatal', max_length=30, verbose_name='Accident Type')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('cause', models.CharField(choices=[('Fall of material', 'Fall of material'), ('Material handling', 'Material handling'), ('Road incident', 'Road incident'), ('Slip', 'Slip'), ('Fall of person', 'Fall of person'), ('Burn', 'Burn'), ('Electrocution', 'Electrocution'), ('Gas exposure', 'Gas exposure'), ('Hit/Caught/Pressed', 'Hit/Caught/Pressed')], default='Slip', max_length=100, verbose_name='Cause')),
                ('narrative', models.TextField(verbose_name='Narrative')),
                ('learning_point', models.CharField(blank=True, max_length=50, verbose_name='Learning Point')),
            ],
            options={
                'verbose_name_plural': 'Accident Details',
            },
        ),
        migrations.CreateModel(
            name='emp_details',
            fields=[
                ('unit_name', models.CharField(max_length=30, verbose_name='Unit Name')),
                ('emp_id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('emp_type', models.CharField(choices=[('Regular', 'Regular'), ('Contract', 'Contract')], default='Regular', max_length=20, verbose_name='Employee Type')),
                ('emp_name', models.CharField(max_length=30, verbose_name='Employee Name')),
                ('age', models.PositiveSmallIntegerField(default='21', validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(80)], verbose_name='Age')),
                ('dept', models.CharField(max_length=20, verbose_name='Department')),
                ('shift', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('G', 'G')], default='A', max_length=5, verbose_name='Shift')),
            ],
            options={
                'verbose_name_plural': 'Employee Details',
            },
        ),
        migrations.DeleteModel(
            name='FatalAccident',
        ),
        migrations.DeleteModel(
            name='FirstAid',
        ),
        migrations.DeleteModel(
            name='NonReportable',
        ),
        migrations.DeleteModel(
            name='Reportable',
        ),
        migrations.AddField(
            model_name='accd_details',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accd_emp_id', to='InputForms.emp_details'),
        ),
    ]
