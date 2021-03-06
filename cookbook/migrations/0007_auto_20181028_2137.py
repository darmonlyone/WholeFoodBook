# Generated by Django 2.1.2 on 2018-10-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0006_auto_20181028_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='allergies_tags',
            field=models.ManyToManyField(blank=True, related_name='allergiess', to='cookbook.Allergies'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='equipment_tags',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='cookbook.Equipment'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_tags',
            field=models.ManyToManyField(blank=True, related_name='cook_times', to='cookbook.CookTime'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='category_tags',
            field=models.ManyToManyField(related_name='categories', to='cookbook.Category'),
        ),
    ]
