# Generated by Django 3.0.8 on 2020-07-28 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191216_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_publish']},
        ),
    ]
