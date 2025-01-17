# Generated by Django 4.0.9 on 2023-02-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarket', '0006_remove_rate_html_raw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='circulating_supply',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rate',
            name='market_dominance',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rate',
            name='max_supply',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rate',
            name='total_supply',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rate',
            name='volume_market_cap',
            field=models.CharField(max_length=50),
        ),
    ]
