# Generated by Django 2.1.2 on 2018-11-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='des',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='push_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
