# Generated by Django 2.1.1 on 2018-10-22 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='user',
            new_name='recipe_chef',
        ),
    ]
