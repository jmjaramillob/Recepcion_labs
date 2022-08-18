# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('departure_time', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=10, unique=True)),
                ('pc_disp', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=60)),
                ('cod', models.CharField(default='None', max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(default='None', max_length=60)),
                ('ced', models.CharField(default='-1', max_length=60, primary_key=True, serialize=False, unique=True)),
                ('cod', models.CharField(default='None', max_length=60, unique=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Program')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='pc',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='registro.Pc'),
        ),
        migrations.AddField(
            model_name='loan',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='registro.Student'),
        ),
    ]
