# Generated by Django 5.0.6 on 2024-05-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0003_alter_slider_image_alter_slider_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='uploads/slider', verbose_name='تصویر'),
        ),
    ]
