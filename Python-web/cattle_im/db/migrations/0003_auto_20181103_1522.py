# Generated by Django 2.1.2 on 2018-11-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20181103_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(0, '男'), (1, '女')], null=True),
        ),
    ]