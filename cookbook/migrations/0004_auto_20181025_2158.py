# Generated by Django 2.1.1 on 2018-10-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0003_recipe_recipe_image_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image_2',
            field=models.ImageField(blank=True, upload_to='recipe_image/'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_image_3',
            field=models.ImageField(blank=True, upload_to='recipe_image/'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_image_4',
            field=models.ImageField(blank=True, upload_to='recipe_image/'),
        ),
    ]
