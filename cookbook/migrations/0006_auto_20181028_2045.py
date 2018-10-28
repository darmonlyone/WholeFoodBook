# Generated by Django 2.1.2 on 2018-10-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_auto_20181025_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergies_ingredient', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CookTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_required', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='allergies_tags',
            field=models.ManyToManyField(related_name='allergiess', to='cookbook.Allergies'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='equipment_tags',
            field=models.ManyToManyField(related_name='equipments', to='cookbook.Equipment'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_tags',
            field=models.ManyToManyField(related_name='cook_times', to='cookbook.CookTime'),
        ),
    ]