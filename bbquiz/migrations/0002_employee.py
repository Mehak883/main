# Generated by Django 4.1.7 on 2023-06-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbquiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('auth_token', models.CharField(max_length=100)),
                ('user_profile_image', models.ImageField(upload_to='')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('emp_id', models.CharField(max_length=8)),
            ],
        ),
    ]
