# Generated by Django 4.1.7 on 2023-07-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbhome', '0040_alter_query_ctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='replied_by',
            field=models.EmailField(blank=True, default='-1', max_length=100),
        ),
        migrations.DeleteModel(
            name='replied',
        ),
    ]
