# Generated by Django 3.0.5 on 2020-04-14 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200414_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='description_ua',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_ua',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_ua',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ua',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_ua',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_ua',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country_ua',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description_ua',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline_ua',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title_ua',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='description_ua',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='title_ua',
        ),
    ]
