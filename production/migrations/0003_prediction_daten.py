# Generated by Django 2.2.4 on 2020-04-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20200428_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='daten',
            field=models.DateField(auto_now=True),
        ),
    ]
