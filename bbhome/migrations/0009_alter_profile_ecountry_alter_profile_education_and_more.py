# Generated by Django 4.1.7 on 2023-06-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbhome', '0008_rename_institute_profile_ecountry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ecountry',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ins_name',
            field=models.CharField(max_length=100),
        ),
    ]
