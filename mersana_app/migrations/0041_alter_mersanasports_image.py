# Generated by Django 5.0.6 on 2024-06-13 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0040_alter_aboutus_description_alter_aboutus_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mersanasports',
            name='image',
            field=models.ImageField(upload_to='uploads/mersana_sports', verbose_name='تصویر'),
        ),
    ]
