# Generated by Django 4.1.6 on 2023-02-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.TextField(blank=True, null=True, verbose_name='Images'),
        ),
    ]
