# Generated by Django 4.1.7 on 2023-08-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbhome', '0043_ranking_gift_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cprice',
            field=models.IntegerField(default=0),
        ),
    ]
