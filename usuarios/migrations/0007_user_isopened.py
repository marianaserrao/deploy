# Generated by Django 3.0.5 on 2020-05-12 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20200511_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isOpened',
            field=models.BooleanField(default=True),
        ),
    ]
