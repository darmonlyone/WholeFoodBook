# Generated by Django 2.1.2 on 2018-11-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0008_auto_20181029_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image_1',
            field=models.ImageField(blank=True, upload_to='recipe_image/'),
        ),
    ]