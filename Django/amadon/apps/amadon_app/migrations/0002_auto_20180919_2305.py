# Generated by Django 2.1.1 on 2018-09-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amadon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]