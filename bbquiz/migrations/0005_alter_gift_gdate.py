# Generated by Django 4.1.7 on 2023-07-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbquiz', '0004_gift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='gdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]