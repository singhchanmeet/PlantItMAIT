# Generated by Django 4.1.4 on 2022-12-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_plant_plant_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='plant_description',
        ),
        migrations.AddField(
            model_name='plant',
            name='lant_descriptionp',
            field=models.CharField(default='', max_length=1000),
        ),
    ]