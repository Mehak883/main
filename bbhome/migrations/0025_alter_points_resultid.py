# Generated by Django 4.1.7 on 2023-07-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbhome', '0024_customuser_is_employee_customuser_is_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='resultid',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
