# Generated by Django 2.2.4 on 2019-12-27 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentbook', '0003_auto_20191223_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(verbose_name='Post description'),
        ),
        migrations.CreateModel(
            name='coment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='message')),
                ('date_coment', models.DateField(default=datetime.date.today)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentbook.Blog')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentbook.User')),
            ],
        ),
    ]