# Generated by Django 2.2.4 on 2019-12-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentbook', '0002_auto_20191223_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Post description'),
        ),
    ]
