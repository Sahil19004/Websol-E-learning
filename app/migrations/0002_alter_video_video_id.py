# Generated by Django 4.1.2 on 2023-05-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]