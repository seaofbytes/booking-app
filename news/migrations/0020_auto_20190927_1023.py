# Generated by Django 2.1.8 on 2019-09-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20190927_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='article',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
