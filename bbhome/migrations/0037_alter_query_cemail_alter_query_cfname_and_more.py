# Generated by Django 4.1.7 on 2023-07-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbhome', '0036_query_replied_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='cemail',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='cfname',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='clname',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='replied_by',
            field=models.CharField(blank=True, default='-1', max_length=100),
        ),
    ]