# Generated by Django 2.1.2 on 2019-12-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]