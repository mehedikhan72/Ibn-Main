# Generated by Django 4.1.4 on 2023-06-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0036_ouds_cover_image2_alter_tracker_delivary_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeBorad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=500)),
            ],
        ),
    ]
