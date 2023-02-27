# Generated by Django 4.0.9 on 2023-02-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarket', '0003_cryptocurrency_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='name',
            field=models.CharField(db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
