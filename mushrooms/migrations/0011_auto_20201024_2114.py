# Generated by Django 3.1.1 on 2020-10-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushrooms', '0010_auto_20201023_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borowik',
            old_name='hat',
            new_name='description_hat',
        ),
        migrations.RenameField(
            model_name='borowik',
            old_name='pulp',
            new_name='description_pulp',
        ),
        migrations.RenameField(
            model_name='borowik',
            old_name='shaft',
            new_name='description_shaft',
        ),
        migrations.RenameField(
            model_name='mushroom',
            old_name='hat',
            new_name='description_hat',
        ),
        migrations.RenameField(
            model_name='mushroom',
            old_name='pulp',
            new_name='description_pulp',
        ),
        migrations.RenameField(
            model_name='mushroom',
            old_name='shaft',
            new_name='description_shaft',
        ),
        migrations.AddField(
            model_name='borowik',
            name='area_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='area_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='base_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='color_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='color_pulp',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='color_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='fruitcake',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='habitat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='incidence_time',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='milk',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='rim_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='section_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='shape_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='shape_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='borowik',
            name='type_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='area_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='area_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='base_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='color_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='color_pulp',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='color_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='fruitcake',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='habitat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='incidence_time',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='milk',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='rim_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='section_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='shape_hat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='shape_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='type_shaft',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]