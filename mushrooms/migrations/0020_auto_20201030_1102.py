# Generated by Django 3.1.1 on 2020-10-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushrooms', '0019_auto_20201030_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mushroom',
            name='category',
            field=models.CharField(max_length=128),
        ),
    ]