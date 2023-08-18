# Generated by Django 4.1.7 on 2023-07-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbquiz', '0006_delete_gift'),
    ]

    operations = [
        migrations.CreateModel(
            name='gift',
            fields=[
                ('gift_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('gift_pic', models.ImageField(default='giftimg.jpg', upload_to='gifts')),
                ('gname', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('points_needed', models.FloatField()),
                ('rank_needed', models.IntegerField()),
                ('gdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]