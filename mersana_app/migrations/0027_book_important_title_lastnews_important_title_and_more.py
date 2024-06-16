# Generated by Django 5.0.6 on 2024-06-10 15:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0026_remove_lastnews_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastnews',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanacreativity',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanafriends',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanamusic',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanapaints',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanapiano',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanaschool',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanasports',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mersanatrip',
            name='important_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='تیتر بالا'),
            preserve_default=False,
        ),
    ]
