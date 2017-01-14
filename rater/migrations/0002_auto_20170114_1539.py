# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 15:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChosenMeme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(default='')),
            ],
            options={
                'db_table': 'chosenMemes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='_user_liked_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='matches',
            field=models.ManyToManyField(blank=True, related_name='_user_matches_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meme',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='memes', to='rater.Tag'),
        ),
        migrations.AddField(
            model_name='chosenmeme',
            name='meme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picked_images', to='rater.Meme'),
        ),
        migrations.AddField(
            model_name='chosenmeme',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memes', to=settings.AUTH_USER_MODEL),
        ),
    ]
