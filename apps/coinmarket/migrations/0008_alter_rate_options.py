# Generated by Django 4.0.9 on 2023-02-27 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coinmarket', '0007_alter_rate_circulating_supply_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'ordering': ['-rate_date']},
        ),
    ]
