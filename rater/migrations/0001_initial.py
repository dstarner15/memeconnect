# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('gender_match', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('a', 'Bread'), ('a', 'All')], default='m', help_text="Gender for the user's match.", max_length=2)),
                ('first_name', models.CharField(default='', help_text="The user's first name.", max_length=128)),
                ('last_name', models.CharField(default='', help_text="The user's last name.", max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
                'verbose_name': 'MemeConnect User',
                'verbose_name_plural': 'MemeConnect Users',
            },
        ),
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256)),
                ('safe_url', models.URLField(default='', help_text="A 'safe' url that will always be a hit. Use KnowYourMeme.", max_length=512)),
            ],
            options={
                'db_table': 'memes',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=128)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='meme',
            name='tags',
            field=models.ManyToManyField(blank=True, to='rater.Tag'),
        ),
    ]
