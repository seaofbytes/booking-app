# Generated by Django 2.1.8 on 2019-09-26 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190923_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img5',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img6',
        ),
    ]
